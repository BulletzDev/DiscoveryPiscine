#!/usr/bin/env python3

def add_one(var1):
    var1 = var1 + 1
    print(f"Inside function, var1 is {var1}")

var1 = 5
add_one(var1)
print(f"Outside function, var1 is {var1}")