#!/usr/bin/env python3

TEMPLATE_VERSION = 'v1-six-page-shared-body-and-head'
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

SHARED_STYLE = "body{font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.75;margin:0;background:#f8faf9;color:#1f2933}.wrap{max-width:960px;margin:0 auto;padding:48px 24px}.hero,.card,article{background:#fff;border:1px solid #d9e2dc;border-radius:18px;padding:28px;box-shadow:0 8px 24px rgba(0,0,0,.04)}h1{font-size:2rem;margin:0 0 14px;color:#123026}h2{font-size:1.2rem;margin-top:1.4em;color:#123026}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:22px}a{color:#0f766e;font-weight:700}.meta{color:#52616b;font-size:.95rem}.notice{background:#eef8f1;border-left:6px solid #2f855a;padding:16px 18px;border-radius:10px}.status{display:inline-block;background:#eef8f1;border:1px solid #a7d7bd;color:#0f5132;border-radius:999px;padding:2px 10px;font-size:.85rem;font-weight:700}.pilot{display:inline-block;margin:0 0 10px;color:#0f5132;font-weight:800;letter-spacing:.02em}.lead{font-size:1.08rem;font-weight:700}.core{margin-top:18px;padding:18px;border:1px solid #d9e2dc;border-radius:14px;background:#fbfdfc}"

CHILD_CARDS = [
    ('人間向け要約', '初見者へ価値核、中心因果線、判断方法を渡す要約。', 'ja/human-summary/', '読む'),
    ('FAQ', '誤読防止と境界条件を扱うFAQ。', 'ja/faq/', '読む'),
    ('日本語AI索引', 'AI再利用時の定義、判断条件、制約。', 'ja/ai-index/', '読む'),
    ('English AI Index', 'English retrieval and interpretation page.', 'en/ai-index/', 'Open'),
    ('中文AI索引', '中文检索和解释页面。', 'zh/ai-index/', '打开'),
]


def assert_contract():
    if TEMPLATE_VERSION != 'v1-six-page-shared-body-and-head':
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
