#!/usr/bin/env python3
import sys
params = sys.argv

def shrkin(var1):
    return var1[:8]

def enlarge(var1):
    if len(var1) < 8:
        return var1 + "z" * (8 - len(var1))
    return var1

def process_string(var1):
    if len(var1) > 8:
        return shrkin(var1)
    elif len(var1) < 8:
        return enlarge(var1)
    else:
        return var1
    
process_strings = [process_string(param) for param in params[1:]]
for result in process_strings:
    print(result)