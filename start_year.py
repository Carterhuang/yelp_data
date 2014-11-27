#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from heapq import heappush, heappop


year_map = {}

with open(sys.argv[1], 'r') as f:
    review_data = f.readline().encode('utf8')

    while review_data:
        try:
            js  = json.loads(review_data)
        except ValueError:
            continue
        try:
            date = int(js.get('date')[0:4])
            business = js.get('business_id')
        except UnicodeEncodeError:
            continue

        if business not in year_map:
            year_map[business] = date
        elif date < year_map[business]:
            year_map[business] = date

        review_data = f.readline().encode('utf8')


with open(sys.argv[2], 'w') as fout:
    for k in year_map:
        fout.write("%s, %d\n"%(k, year_map[k])) 
     

