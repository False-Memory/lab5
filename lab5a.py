# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 18th, 2024
# Purpose: Read a text file.
# Usage: ./lab4a.py

# TO DO 1: Create data2.txt.

# TO DO 2: Complete the functions below.

def read_file_lineByLine(file_name):
    # Takes file_name as a string, read the file in a loop one line at a time and print each line as you read it.
    with open(file_name) as dataFile:
        data = dataFile.read()
        print(data)


def read_file_list(file_name):
    # Takes a file_name as string, read file line by line and add the line in a list as a list element without new-line characters
    # Return the list.
    with open(file_name) as Listfile:
        list = []
        for i in Listfile:
            list.append(i.strip())
        return list


def main():
    file_name = 'data.txt'
    file_2 = 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))

    read_file_lineByLine(file_2)
    print(read_file_list(file_2))

main()