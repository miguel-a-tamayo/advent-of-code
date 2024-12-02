import sys
import re

def main(filename: str) -> None:
    list1 = []
    list2 = []

    # collect data
    with open(filename, "r") as input_file:
        for line in input_file:
            splitLine = line.split(" ")

            list1.append(int(splitLine[0]))
            list2.append(int(splitLine[-1]))
    
    list1.sort()
    list2.sort()

    distances = [abs(a - b) for a, b in zip(list1, list2)]
    totalDistance = sum(distances)

    print("Total Distance:", totalDistance)
    return None

    
if __name__=="__main__":
    main(sys.argv[1])
    