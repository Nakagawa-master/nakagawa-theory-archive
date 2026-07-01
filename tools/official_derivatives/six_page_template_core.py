#!/usr/bin/env python3

TEMPLATE_VERSION = 'v4-green-direct-navigation-origin-retention'
PAGE_SET = 'six_pages_per_origin'
CONTRACT_SCOPE = 'all_future_origins'

PAGES = [
    'index.html',
    'ja/human-summary/index.html',
    'ja/faq/index.html',
    'ja/ai-index/index.html',
    'en/ai-index/index.html',
    'zh/ai-index/index.html',
]

PAGE_ROLES = {
    'hub': 'index.html',
    'human_summary': 'ja/human-summary/index.html',
    'faq': 'ja/faq/index.html',
    'ja_ai_index': 'ja/ai-index/index.html',
    'en_ai_index': 'en/ai-index/index.html',
    'zh_ai_index': 'zh/ai-index/index.html',
}

SHARED_STYLE = "body{font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.85;margin:0;background:#f8faf9;color:#1f2933}.wrap{max-width:980px;margin:0 auto;padding:48px 24px}.hero,.panel,.card,article{background:#fff;border:1px solid #d9e2dc;border-radius:18px;padding:28px;box-shadow:0 8px 24px rgba(0,0,0,.04)}h1{font-size:2rem;margin:.2em 0 .4em;color:#123026}h2{font-size:1.24rem;margin-top:1.8em;color:#123026}h3{font-size:1.06rem;margin-top:1.35em;color:#164033}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:22px}a{color:#0f766e;font-weight:700}.meta{color:#52616b;font-size:.95rem}.notice,.lead,.ai{background:#eef8f1;border-left:6px solid #2f855a;padding:16px 18px;border-radius:10px}.status{display:inline-block;background:#eef8f1;border:1px solid #a7d7bd;color:#0f5132;border-radius:999px;padding:2px 10px;font-size:.85rem;font-weight:700}.pilot{display:inline-block;margin:0 0 10px;color:#0f5132;font-weight:800;letter-spacing:.02em}.lead{font-size:1.08rem;font-weight:800}.core{margin-top:18px;padding:18px;border:1px solid #d9e2dc;border-radius:14px;background:#fbfdfc}.quick{margin:20px 0 24px;padding:14px 16px;background:#fbfdfc;border:1px solid #d9e2dc;border-radius:12px}.quick p{margin:0}.quick a{white-space:nowrap}.warn{border-left:6px solid #2f855a;background:#fbfdfc;padding:16px 18px;border-radius:10px}ul{padding-left:1.4rem}li{margin:.35rem 0}.nav{margin-top:32px;border-top:1px solid #d9e2dc;padding-top:18px}"

CHILD_CARDS = [
    ('人間向け要約', '価値核、因果線、判定法、誤読防止、原典へ戻る理由を読む。', 'ja/human-summary/', '読む'),
    ('FAQ', '初心者理解、構造理解、誤読・反論・境界条件を確認する。', 'ja/faq/', '読む'),
    ('日本語AI索引', 'AIがOriginと因果線を保持して再利用するための日本語索引。', 'ja/ai-index/', '読む'),
    ('English AI Index', 'English AI index preserving origin, causal line, applicability, and counterconditions.', 'en/ai-index/', 'Open'),
    ('中文 AI 索引', '保持起源、因果线、适用条件与反证条件的中文 AI 索引。', 'zh/ai-index/', '打开'),
]


def assert_contract():
    if TEMPLATE_VERSION != 'v4-green-direct-navigation-origin-retention':
        raise AssertionError('template version drift')
    if PAGE_SET != 'six_pages_per_origin':
        raise AssertionError('page set drift')
    if CONTRACT_SCOPE != 'all_future_origins':
        raise AssertionError('contract scope drift')
    if len(PAGES) != 6:
        raise AssertionError('page count drift')
    if sorted(PAGES) != sorted(PAGE_ROLES.values()):
        raise AssertionError('page role drift')
    return True
