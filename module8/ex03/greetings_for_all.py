#!/usr/bin/env python3

def greetings(var1="noble stranger"):
    if not isinstance(var1, str):
        return "Error: Input must be a string"
    return f"Hello, {var1}"

print(greetings(23))
print(greetings())
print(greetings("Max"))