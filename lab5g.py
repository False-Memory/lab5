# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 18, 2024
# Purpose: Handle ValueError
# Usage: ./lab4g.py

# TO DO 1: Complete the given functions.

def double_number(n):
  # double the number n
  # Add an exception block to handle the error if n is not a number
  # Except block should display the appropriate error messages
  try:
    print(int(n)*2)
  except ValueError:
    print("Exception: ValueError")

def main():
  double_number(3)  # works
  double_number('v') # exception : ValueError
  
# TO DO 2: Run the script.
main()