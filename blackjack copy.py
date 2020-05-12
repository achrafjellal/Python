#!/usr/bin/env python3

import requests
import sys
import re

url=sys.argv[1]

s = requests.Session()
r = s.get(url)
x = 0 
while r.text.find('RCN') == -1 :
    
    r = s.post(f'{url}/bj.php', data = {'do_what':'deal'})
    #print(r.text)
    flag = re.findall('{"flag":"(.*)"}', r.text)    
print(flag[0])
