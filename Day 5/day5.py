import re

crate1 = ['S', 'C', 'V', 'N']
crate2 = ['Z', 'M', 'J', 'H', 'N', 'S']
crate3 = ['M', 'C', 'T', 'G', 'J', 'N', 'D']
crate4 = ['T', 'D', 'F', 'J', 'W', 'R', 'M']
crate5 = ['P', 'F', 'H']
crate6 = ['C', 'T', 'Z', 'H', 'J']
crate7 = ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z']
crate8 = ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W']
crate9 = ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
movedCrates = []
test = [3, 9, 6]

def moveCrates(qty, start, end):
    #print(f"Moving {qty} crates from stack {start} to stack {end}.")
    startStack = determineStack(start)
    endStack = determineStack(end)
    #print(startStack)
    #print(endStack)
    x = 1
    while x <= qty:
        endStack.append(startStack[-1])
        startStack.pop(-1)
        #print('\n')
        #print (startStack)
        #print (endStack)
        x = x + 1
    
def determineStack(stack):
    if stack == 1:
        return crate1
    if stack == 2:
        return crate2
    if stack == 3:
        return crate3
    if stack == 4:
        return crate4
    if stack == 5:
        return crate5
    if stack == 6:
        return crate6
    if stack == 7:
        return crate7
    if stack == 8:
        return crate8
    if stack == 9:
        return crate9
        
    
#moveCrates(test[0], test[1], test[2])

#moveCrates(7, 6, 2)
temp = []
with open('input.txt', 'rt') as f:
    for line in f:
        #print("Original string : " + line) 
 
        temp = re.findall(r'\d+', line) 
        #print (temp)
        moveCrates(int(temp[0]), int(temp[1]), int(temp[2]))
 
print (f"Result: {crate1[-1]}{crate2[-1]}{crate3[-1]}{crate4[-1]}{crate5[-1]}{crate6[-1]}{crate7[-1]}{crate8[-1]}{crate9[-1]}")