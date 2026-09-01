#!/usr/bin/env python3
"""Resolve citation tokens in the report draft into a single global reference list.
Tokens look like [W1-R5], [W2b-R3], [V-R2]; multiple may be chained: [W1-R5][W5-R2].
Sources are parsed from each findings file, from the text after its last '## 來源' heading.
Usage: build_report.py draft.md out.md
"""
import re, sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = {
    'W1': 'findings/WP-1_major_domestic.md',
    'W2': 'findings/WP-2_midtier_pc.md',
    'W2b': 'findings/WP-2b_bancassurance.md',
    'W3': 'findings/WP-3_foreign.md',
    'W4': 'findings/WP-4_online_new.md',
    'W5': 'findings/WP-5_market_special.md',
    'V': 'findings/V_verification.md',
}
def load_sources(path):
    txt = open(path, encoding='utf-8').read()
    idx = txt.rfind('## 來源')
    body = txt[idx:] if idx >= 0 else txt
    out = {}
    for line in body.splitlines():
        m = re.match(r'^\s*-?\s*\[R(\d+)\]\s*(.+?)\s*$', line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out
sources = {k: load_sources(os.path.join(BASE, v)) for k, v in FILES.items() if os.path.exists(os.path.join(BASE, v))}
draft = open(sys.argv[1], encoding='utf-8').read()
order = []; num = {}
def repl(m):
    key = (m.group(1), int(m.group(2)))
    if key not in num:
        if key[0] not in sources or key[1] not in sources[key[0]]:
            sys.stderr.write(f'WARNING unresolved {key}\n'); return m.group(0)
        order.append(key); num[key] = len(order)
    return f'[{num[key]}]'
out = re.sub(r'\[(W1|W2b|W2|W3|W4|W5|V)-R(\d+)\]', repl, draft)
bib = ['', '## 參考文獻（Reference）', '', '以下編號對應內文之 [n]。「WP-n」為原始調查工單代號，「V」為主代理複核紀錄。所有來源查閱日均為 2026-09-01；受環境限制，URL 之網頁全文未能開啟，僅依搜尋引擎回傳之標題、網址與摘要確認。', '']
for i, key in enumerate(order, 1):
    bib.append(f'[{i}] {sources[key[0]][key[1]]}　（{key[0].replace("W","WP-")}-R{key[1]}）')
out = out.rstrip() + '\n' + '\n'.join(bib) + '\n'
open(sys.argv[2], 'w', encoding='utf-8').write(out)
print(f'resolved {len(order)} references')
