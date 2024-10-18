# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian 
# Date: October 18th, 2024
# Purpose: Write data to a file.
# Usage: ./lab4b.py

# TO DO 1: Paste the code provided in readme.md file.
f = open('fruits.txt', 'w')

# TO DO 2: Run the script.

# TO DO 3: Run the 'ls' command.

# TO DO 4: Paste the code provided in readme.md file.

f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?')
f.close()

# TO DO 5: Print the contents of fruits.txt.
with open("fruits.txt") as read:
    for i in read:
        print(i.strip())