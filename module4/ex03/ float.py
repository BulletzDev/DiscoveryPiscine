#!/usr/bin/env python3
import math
while True:
    user_input1 = input("Enter the number: ")
    try:
        user_input1 =  float(user_input1) 
        break
    except ValueError:
        print("This isn't a valid number.")

if user_input1-math.floor(user_input1)>0:
    print("Its a float number")
else:
    print("Its an integer number")