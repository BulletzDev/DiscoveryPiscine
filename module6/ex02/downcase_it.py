#!/usr/bin/env python3
import sys

params = sys.argv

if len(params) == 2:
    print(params[1].lower()+"\n")
else:
    print("none\n")
