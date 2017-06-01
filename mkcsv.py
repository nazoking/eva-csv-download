# -*- coding: utf-8 -*-

import sys
import re
import csv

finder = re.compile(r"""(.*?)「(.*)」 *$""")
titlef = re.compile(r"""^(?:新世紀エヴァンゲリオン　)(.*)(　全セリフ)?""")

w = csv.writer(sys.stdout)
w.writerow(['Title', 'Name', 'Line'])
for line in sys.stdin.readlines():
    line = line.strip()
    if '2. エヴァ|' == line:
        title = None
        continue
    m = titlef.match(line)
    if m:
        title = m.group(1)
        continue
    if line == 'ヱヴァンゲリヲン新劇場版：序　全セリフ':
        title = 'ヱヴァンゲリヲン新劇場版：序'
        continue
    m = finder.match(line)
    if m and m.group(2).strip():
        w.writerow([title, m.group(1).strip(), m.group(2).strip()])
