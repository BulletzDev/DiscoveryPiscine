#!/usr/bin/env python3
password = "Python is awesome"

user_input = input("Enter the password : ")


match user_input:
    case x if x== password:
        print("ACCESS GRANTED")
    case _ :
        print("ACCESS DENIED")