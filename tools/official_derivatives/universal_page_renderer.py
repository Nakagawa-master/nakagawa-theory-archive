#!/usr/bin/env python3
import html

from six_page_template_core import CHILD_CARDS, PAGE_ROLES, PAGES, SHARED_STYLE, assert_contract
from universal_renderer_contract import assert_input


def e(value):
    return html.escape(str(value or ''), quote=True)


def p(text):
    return '<p>' + e(text) + '</p>'


def status_for(path):
    return '公式派生物一覧' if path == 'index.html' else '公式派生物'


def hub_url(record):
    return '/derivatives/' + record['folder_id'] + '/'


def origin_line(record):
    return '<p>原典: <a href="' + e(record['parent_url']) + '">' + e(record['parent_title']) + '</a></p>'


def identity_line(record):
    return '<p class="meta">Parent NCL-ID: ' + e(record['parent_ncl_id']) + '<br>Parent Diff-ID: ' + e(record['parent_diff_id']) + '</p>'


def hero(record, path, title):
    return '<section class="hero"><p class="status">' + e(status_for(path)) + '</p><p class="pilot">' + e(record['slot_id']) + '</p><h1>' + e(title) + '</h1>' + identity_line(record) + origin_line(record) + '</section>'


def nav(record):
    return '<nav aria-label="Derivative navigation"><p><a href="' + e(hub_url(record)) + '">← ' + e(record['slot_id']) + 'の公式派生物一覧へ戻る</a></p><p><a href="/derivatives/">公式派生物一覧へ戻る</a></p></nav>'


def child_cards(record):
    cards = []
    for label, text, href, action in CHILD_CARDS:
        cards.append('<article class="card"><h2>' + e(label) + '</h2><p>' + e(text) + '</p><p><a href="' + e(hub_url(record) + href) + '">' + e(action) + '</a></p></article>')
    return ''.join(cards)


def shell(record, path, title, body, head_html=''):
    return '<!doctype html><html lang="ja">' + head_html + '<body><main class="wrap">' + hero(record, path, title) + body + nav(record) + '</main></body></html>\n'


def assert_renderer_contract(record):
    assert_contract()
    assert_input(record)
    if list(PAGE_ROLES.values()) and sorted(PAGES) != sorted(PAGE_ROLES.values()):
        raise AssertionError('page role values mismatch')
    if not SHARED_STYLE:
        raise AssertionError('missing shared style')
    return True
