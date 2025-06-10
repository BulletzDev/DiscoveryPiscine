#!/usr/bin/env python3
import sys
import re

params = sys.argv[1:]

if len(params) == 0 or len(params)>1 or "z" not in params[0]:
    print("none\n")

final = re.sub("[^z]", "", params[0])
print(final)