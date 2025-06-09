#!/usr/bin/env python3
numbers = [4, 20, 2, 4210,2,4]

final_set = {2}
final_set.update(numbers)

modified_set = {x + 2 if x > 5 else x for x in final_set}

print(f"original array : {numbers}")
print(f"final array : {modified_set}")
