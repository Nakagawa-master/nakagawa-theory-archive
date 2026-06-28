#!/usr/bin/env python3
from pathlib import Path
import re, html, json, sys

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS_FILE = Path(__file__).resolve().with_name('targets.tsv')
DEFAULT_PILOTS = ['ncl-alpha-20251124-e4c70c','ncl-alpha-20260517-b80e39','ncl-alpha-20260627-aea14a','ncl-alpha-20260617-d0b342']
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']
TEMPLATE_VERSION = 'v1-six-page-shared-body-and-head'
REQUIRED = ['description','canonical','derivative-type','derivative-scope','language','parent-url','parent-ncl-id','parent-diff-id','pilot-id','render-status','origin-author','source-archive','ai-purpose','ai-summary','ai-interpretation-warning','ai-reuse-constraint','ai-origin-policy','ai-citation-requirement','og:title','twitter:card','application/ld+json','official-derivative-template-version']

def esc(s): return html.escape(s or '', quote=True)
def one(p,s,d=''):
    m=re.search(p,s,re.S|re.I); return html.unescape(m.group(1)) if m else d
def meta(n,s,d=''):
    return one(r'<meta\s+name=["\']'+re.escape(n)+r'["\']\s+content=["\'](.*?)["\']',s,d)
def prop(n,s,d=''):
    return one(r'<meta\s+property=["\']'+re.escape(n)+r'["\']\s+content=["\'](.*?)["\']',s,d)
def style(s):
    m=re.search(r'<style>.*?</style>',s,re.S|re.I); return m.group(0) if m else '<style>body{font-family:system-ui;line-height:1.8}</style>'
def lang(rel,s):
    if rel.startswith('en/'): return 'en'
    if rel.startswith('zh/'): return 'zh'
    return meta('language',s,'ja')
def dtype(rel):
    if rel=='index.html': return 'official_derivative_hub'
    if 'human-summary' in rel: return 'human_summary'
    if 'faq' in rel: return 'faq'
    return 'ai_index'
def purpose(rel):
    if rel=='index.html': return 'official derivative hub for human and AI retrieval'
    if 'human-summary' in rel: return 'official human summary for human and AI retrieval'
    if 'faq' in rel: return 'official FAQ for human and AI retrieval'
    if rel.startswith('en/'): return 'official English AI index for retrieval and interpretation'
    if rel.startswith('zh/'): return 'official Chinese AI index for retrieval and interpretation'
    return 'official Japanese AI index for retrieval and interpretation'
def locale(l): return {'ja':'ja_JP','en':'en_US','zh':'zh_CN'}.get(l,'ja_JP')
def robots_for(status): return 'noindex,nofollow' if status == 'staged' else 'index,follow'
def render_status_for(status): return 'official_derivative_staged_nonindexable' if status == 'staged' else 'official_derivative_active_indexable'

def parse_args(args):
    status='active'; explicit=[]
    for a in args:
        if a.startswith('--status='): status=a.split('=',1)[1]
        elif a: explicit.append(a)
    return status, explicit

def load_targets(args):
    status, explicit = parse_args(args)
    if explicit: return status, explicit
    if not TARGETS_FILE.exists(): return status, DEFAULT_PILOTS
    rows=[]
    for line in TARGETS_FILE.read_text(encoding='utf-8').splitlines()[1:]:
        if not line.strip(): continue
        parts=line.split('\t')
        if len(parts) >= 2: rows.append({'folder_id':parts[0].strip(),'export_status':parts[1].strip()})
    return status, [r['folder_id'] for r in rows if r['export_status']==status]

def render_head(s, rel, status):
    title=one(r'<title>(.*?)</title>',s,'Official derivative')
    desc=meta('description',s,title)
    canon=one(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']',s)
    l=lang(rel,s)
    parent_url=meta('parent-url',s)
    parent_ncl=meta('parent-ncl-id',s)
    parent_diff=meta('parent-diff-id',s)
    pilot=meta('pilot-id',s)
    parent_title=one(r'<p>原典: <a [^>]+>(.*?)</a>',s,title)
    ai_warning=meta('ai-interpretation-warning',s,'Keep the parent article context and page role attached.')
    ai_reuse=meta('ai-reuse-constraint',s,'Preserve parent_url, parent_ncl_id, parent_diff_id, derivative_type and canonical URL.')
    site=prop('og:site_name',s,'中川マスター公式アーカイブ')
    data={'@context':'https://schema.org','@type':'WebPage','name':title,'description':desc,'url':canon,'isPartOf':{'@type':'WebSite','name':'中川マスター公式アーカイブ','url':'https://master.ricette.jp/'},'about':parent_title,'author':{'@type':'Person','name':'Nakagawa Master'},'inLanguage':l,'mainEntity':{'@type':'CreativeWork','name':parent_title,'url':parent_url},'identifier':[parent_ncl,parent_diff],'isBasedOn':parent_url}
    lines=[
        '<head>','  <meta charset="utf-8">','  <meta name="viewport" content="width=device-width, initial-scale=1">',f'  <meta name="robots" content="{robots_for(status)}">',
        f'  <title>{esc(title)}</title>',f'  <meta name="description" content="{esc(desc)}">',f'  <link rel="canonical" href="{esc(canon)}">',f'  <meta name="derivative-type" content="{dtype(rel)}">','  <meta name="derivative-scope" content="official_derivative_from_origin_article">',f'  <meta name="language" content="{l}">',
        f'  <meta name="parent-url" content="{esc(parent_url)}">',f'  <meta name="parent-ncl-id" content="{esc(parent_ncl)}">',f'  <meta name="parent-diff-id" content="{esc(parent_diff)}">',f'  <meta name="pilot-id" content="{esc(pilot)}">',f'  <meta name="render-status" content="{render_status_for(status)}">','  <meta name="origin-author" content="Nakagawa Master">','  <meta name="source-archive" content="master.ricette.jp">',
        f'  <meta name="ai-purpose" content="{purpose(rel)}">',f'  <meta name="ai-summary" content="{esc(desc)}">',f'  <meta name="ai-interpretation-warning" content="{esc(ai_warning)}">',f'  <meta name="ai-reuse-constraint" content="{esc(ai_reuse)}">','  <meta name="ai-origin-policy" content="Preserve Origin and parent article context.">','  <meta name="ai-citation-requirement" content="Keep parent URL, NCL-ID, Diff-ID and canonical derivative URL attached.">',
        f'  <meta name="official-derivative-template-version" content="{TEMPLATE_VERSION}">','  <meta name="official-derivative-page-set" content="six_pages_per_origin">','  <meta property="og:type" content="article">',f'  <meta property="og:title" content="{esc(title)}">',f'  <meta property="og:description" content="{esc(desc)}">',f'  <meta property="og:url" content="{esc(canon)}">',f'  <meta property="og:site_name" content="{esc(site)}">',f'  <meta property="og:locale" content="{locale(l)}">','  <meta name="twitter:card" content="summary">',f'  <meta name="twitter:title" content="{esc(title)}">',f'  <meta name="twitter:description" content="{esc(desc)}">','  '+style(s),
        '  <script async src="https://www.googletagmanager.com/gtag/js?id=G-BN0BY8C838"></script>',"  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-BN0BY8C838');</script>","  <script type=\"text/javascript\">(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a]||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src='https://www.clarity.ms/tag/'+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,'clarity','script','lkf0sdpw8r');</script>",'  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7505659945932614" crossorigin="anonymous"></script>','  <script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,separators=(',',':'))+'</script>','</head>'
    ]
    return '\n'.join(lines)

def main():
    changed=[]; errors=[]; status, targets=load_targets(sys.argv[1:])
    for root in targets:
        for rel in PAGES:
            p=BASE/root/rel
            if not p.exists(): errors.append('missing '+str(p)); continue
            s=p.read_text(encoding='utf-8')
            if '</head>' not in s: errors.append('no head '+str(p)); continue
            ns=re.sub(r'<head>.*?</head>',render_head(s,rel,status),s,count=1,flags=re.S|re.I)
            for r in REQUIRED:
                if r not in ns: errors.append(str(p)+' missing '+r)
            if ns!=s: p.write_text(ns,encoding='utf-8'); changed.append(str(p))
    if errors:
        print('\n'.join(errors)); return 1
    print('validated_pages='+str(len(targets)*len(PAGES)))
    print('changed_files='+str(len(changed)))
    print('target_status='+status)
    return 0
if __name__=='__main__': sys.exit(main())
