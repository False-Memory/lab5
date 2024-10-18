# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 18th, 2024
# Purpose: Process File data.
# Usage: ./lab4c.py

# TO DO 1: Run the code provided in readme.md file.
with open("rhyme.txt", "w") as dataFile:
    dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")
# TO DO 2: Open rhyme.txt file.
with open("rhyme.txt", "r") as read:
    for i in read:
        count = len(i.split())
        print((i.strip()).strip("."), "---", count, "words")

# TO DO 3: Print the output as directed in readme.md file.
