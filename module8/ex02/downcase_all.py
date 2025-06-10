#!/usr/bin/env python3
import sys

params = sys.argv[1:]

def downcase_it(var1):
    return [x.lower() for x in var1]

x = downcase_it(params)
for i in x:
    print(i)
