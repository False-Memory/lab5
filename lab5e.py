# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Handle FileNotFoundError
# Usage: ./lab4e.py

# TO DO 1: Create text file numbers.txt as directed in readme.md file.

# TO DO 2: Complete the add() functions.

def add(number1, number2):
    # Add two numbers together, return the result, if an error occurs, return the error string generated by the Exception class.
    try:
        return(int(number1) + int(number2))
    except Exception as e:
        return str(e)
# TO DO 3: Complete the read_file() functions.

def read_file(filename):
# Read a file line by line, convert each line to number and return a list of numbers.
# Add two exception blocks, one to handle the error, if error occurs because the file did not exist or file could not be opened. The second except block should handle the exception if data from file could not be converted to integer.
# Both except block should display the appropriate error messages
# Add a finally block which closes the file, if the file was opened successfully.
    numbers = []
    file = None
    try:
        file = open(filename,'r')
        for i in file:
            try:
                num = int(i.strip())
                numbers.append(num)
            except ValueError:
                return(f"Could not convert line to integer: '{i.strip()}'")
    except FileNotFoundError:
        return(f"Error: The file '{filename}' does not exist or could not be opened.")
    except Exception as e:
        return(f"An Error has occured: {e}")
    finally:
        if file:
            file.close()
    

def main():
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('file10000.txt'))       # exception: could not open the file
    print(read_file('numbers.txt'))         # exception: error reading the data

main()