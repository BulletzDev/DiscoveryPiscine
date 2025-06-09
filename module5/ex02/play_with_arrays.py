#!/usr/bin/env python3
numbers = [4,20,2,4210]
final_array = []
for x in numbers:
    if x>5:
        final_array.append(x+2)
    else:
        final_array.append(x)

print(f"original array : {numbers}")
print(f"final array : {final_array}")