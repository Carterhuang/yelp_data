#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from heapq import heappush, heappop


categories_count = {}

with open(sys.argv[1], 'r') as f:
    business_data = f.readline().encode('utf8')
    
    while business_data:
        try:
            js = json.loads(business_data)
        except ValueError:
            continue
        try:
            categories = js.get(sys.argv[3])
        except UnicodeEncodeError:
            # Skip this line
            continue
        
        #categories = categories.split(',')
        #categories = [ category.strip('" ') for category in categories]
        
        for category in categories:
            if category not in categories_count:
                categories_count[category] = 1
            else:
                categories_count[category] += 1

        business_data = f.readline().encode('utf8')

hp = []


for cate, count in categories_count.items():
    heappush(hp, (count * (-1), cate))


with open(sys.argv[2], 'w') as ff:
    while hp:
        item = heappop(hp)
        ff.write('%s %d\n'%(item[1], item[0]*(-1)))
