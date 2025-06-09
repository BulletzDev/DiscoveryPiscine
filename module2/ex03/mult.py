#!/usr/bin/env python3
while True:
    user_input1 = input("Enter a number: ")
    try:
        user_input1 = int(user_input1) 
        break
    except ValueError:
        print("This isn't a valid number.")

while True:
    user_input2 = input("Enter another number: ")
    try:
        user_input2 = int(user_input2) 
        break
    except ValueError:
        print("This isn't a valid number.")

print(f"{user_input1} x {user_input2} = {user_input1*user_input2}")
