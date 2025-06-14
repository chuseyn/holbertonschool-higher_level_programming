#!/usr/bin/python3
for i in range(26):
    if i != 4 and i != 16:  # Skip 'e' (4) and 'q' (16)
        print("{}".format(chr(97 + i)), end="")

