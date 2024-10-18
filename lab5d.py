# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 18th, 2024
# Purpose: Process File data.
# Usage: ./lab4d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.

# TO DO 2: Update each line from pythonStatements.txt and write in output.txt.
f = open('pythonStatements.txt', 'r')
f2 = open('machineCode.txt', 'r')
f3 = open('output.txt', "w")

for i in f:
    f3.write(i[:i.index("#")].strip())
    f3.write("\t")
    f3.write(f2.readline())

# TO DO 3: Run the script.
