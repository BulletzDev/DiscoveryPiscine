#!/usr/bin/env python3
import sys

params = sys.argv[1:]

while True:
    try:
        param1 = int(params[0]) 
        break
    except ValueError:
        print("This isn't a valid number.")

while True:
    try:
        param2 = int(params[1]) 
        break
    except ValueError:
        print("This isn't a valid number.")

if param1>param2:
    param1,param2=param2,param1

final_array =list(range(param1,param2+1))
print(final_array)