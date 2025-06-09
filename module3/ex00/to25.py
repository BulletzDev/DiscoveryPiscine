#!/usr/bin/env python3
while True:
    user_input1 = input("Enter a number: ")
    try:
        user_input1 = int(user_input1) 
        if user_input1 >25:
            raise ValueError
        break
    except ValueError:
        print("This isn't a valid number.") 

for i in range(user_input1,26):
    print(f"Inside the loop, my variable is {i}")