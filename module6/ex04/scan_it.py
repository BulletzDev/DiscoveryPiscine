#!/usr/bin/env python3
import sys
import re

to_search = sys.argv[1]
search_in = sys.argv[2]

tot_params = len(sys.argv)-1

matches = re.findall(to_search, search_in)

if len(sys.argv) != 3:
    print("none")

if not matches:
    print("none")
else:
    print(len(matches))
