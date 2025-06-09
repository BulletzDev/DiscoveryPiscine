#!/usr/bin/env python3
while True:
    user_input = input("Enter a number: ")
    try:
        user_input = int(user_input) 
        break
    except ValueError:
        print("This isn't a valid number.")

for i in range(10,40,10):
    print(f"In {i} years, you'll be {i+int(user_input)} years old")