#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json


checkin_map = {}

with open(sys.argv[1], 'r') as f:
    checkin_data = f.readline().encode('utf8')

    while checkin_data:
        try:
            js  = json.loads(checkin_data)
        except ValueError:
            continue
        try:
            checkins = js.get('checkin_info')
            business = js.get('business_id')
        except UnicodeEncodeError:
            continue

        check_num = 0
        for checkin in checkins:
            check_num += int(checkins.get(checkin))

        checkin_map[business] = check_num

        checkin_data = f.readline().encode('utf8')


with open(sys.argv[2], 'w') as fout:
    for k in checkin_map:
        fout.write("%s, %d\n"%(k, checkin_map[k])) 
     

