import sys
import re
import numpy as np

def main(filename: str) -> None:
    list1 = list()
    list2 = list()

    similarityScore = 0

    # collect data
    with open(filename, "r") as input_file:
        for line in input_file:
            splitLine = line.split(" ")

            list1.append(int(splitLine[0]))
            list2.append(int(splitLine[-1]))

    for number in list1:
        similarityScore += number * list2.count(number)

    print("Similarity Score:", similarityScore)
    return None
    
if __name__=="__main__":
    main(sys.argv[1])
    