#Advent of Code 2022 - Day 3, Challenge 2
#https://adventofcode.com/2022/day/3

# Declare empty list for bag1
bag1 = []
# Declare empty list for bag2
bag2 = []
# Declare empty list for bag3
bag3 = []
# Declare dictionary of item priority value
itemPriority = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
    }
# Declare int to track total priority of all items that are wrong
priorityTotal = 0
file = open("input.txt")

lines = file.readlines()
x = 0
while x < (len(lines)):
    for line in lines[x]:
        line = line.strip('\n')
        for element in range(0, len(line)):
            bag1.append(line[element])
    for line in lines[x+1]:
        line = line.strip('\n')
        for element in range(0, len(line)):
            bag2.append(line[element])
    for line in lines[x+2]:
        line = line.strip('\n')
        for element in range(0, len(line)):
            bag3.append(line[element])
    print(bag1)
    print(bag2)
    print(bag3)
    wrongItem = str(set(bag1).intersection(set(bag2).intersection(bag3)))
    print("The badgeID is: " + wrongItem[2])
    print("It's priority is: " + str(itemPriority[wrongItem[2]]) )
    priorityTotal = priorityTotal + (itemPriority[wrongItem[2]])
    print(priorityTotal)
    bag1 = []
    bag2 = []
    bag3 = []
    x = x + 3
print(priorityTotal)