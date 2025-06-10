#!/usr/bin/env python3
import sys

total_params = sys.argv
param_passed = total_params[1]
param_requested = input("What was the parameter? ")

if total_params>2:
    print("none\n")

match param_passed:
    case x if x== param_requested:
        print("Good job!")
    case _ : 
        print("Nope, sorry!")