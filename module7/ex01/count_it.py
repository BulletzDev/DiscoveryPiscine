#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none\n")

print(f"Parameters : {len(params)}")
for x in params:
    print(f"{x} : {len(x)}")