#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none\n")

for x in params:
    if "ism" not in x:
        print(x+"ism")