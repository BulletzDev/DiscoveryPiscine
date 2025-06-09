#!/usr/bin/env python3
while True:
    user_input1 = input("Enter a number: ")
    try:
        user_input1 = int(user_input1) 
        break
    except ValueError:
        print("This isn't a valid number.")

for i in range(11):
    print(f"{i} x {user_input1} = ", user_input1*i)