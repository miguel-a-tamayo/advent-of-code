"""
Script to create a day folder and the necessary files for advent of code
"""

import os
import sys
import subprocess

def makeFile(path: str) -> None:
    file = open(path, 'w')
    
    to_write = """import sys
import re
import numpy as np

def main(filename: str) -> None:
    pass
    
if __name__=="__main__":
    main(sys.argv[1])
    """

    file.write(to_write)
    file.close()
    print("Created file")


def main(year: int, day: int) -> None:
    curr_path = os.getcwd() # current working directory
    dir_path = curr_path + f"/{year}/day{day}/"

    if os.path.exists(dir_path): # check if directory was already created
        print("Directory already exists. Stopping execution.")
        return

    os.mkdir(dir_path) # make dictionary
    makeFile(dir_path + 'puzzle1.py') # make puzzle 1 file
    makeFile(dir_path + 'puzzle2.py') # make puzzle 2 file

    txt_files = ["example.txt", "input.txt", "problem.txt"]
    for file in txt_files:
        file = open(dir_path + file, "w")
        file.close()

    return None

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])