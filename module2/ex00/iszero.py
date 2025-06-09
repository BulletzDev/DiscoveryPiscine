#!/usr/bin/env python3
while True:
    user_input = input("Enter a number: ")
    try:
        user_input = int(user_input) 
        break
    except ValueError:
        print("This isn't a valid number.")


user_input = int(user_input)

if user_input == 0:
    print("this number is equal to zero")
else:
    print("This number is different from zero")