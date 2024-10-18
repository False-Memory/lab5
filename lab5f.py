# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 18, 2024
# Purpose: Catch ZeroDivisionError
# Usage: ./lab4f.py

# TO DO 1: Complete the given functions.

def safe_divide(a,b):
  # divide a by b
  # Add an exception block to handle the error if error occurs because of a zero denominator.
  # Except block should display the appropriate error messages
  try:
    print(a/b)
  except ZeroDivisionError:
    print("Error, Divison by Zero")


def main():
  safe_divide(10,5)  # works
  safe_divide(10,0)  # exception : Zero Division Error
  
main()