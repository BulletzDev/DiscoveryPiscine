#!/usr/bin/env python3
while True:
    user_input = input("Enter a number: ")
    try:
        user_input = int(user_input) 
        break
    except ValueError:
        print("This isn't a valid number.")

if user_input < 0:
    print("this number is negative")
elif user_input>0:
    print("this number is positive")
else:
    print("this number is both negative and positive")