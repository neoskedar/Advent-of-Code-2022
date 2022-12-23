import re
temp = []
elf1 = []
elf2 = []
overlaps = 0

with open('input.txt', 'rt') as f:
    for line in f:
        print("Original string : " + line) 
 
        temp = re.findall(r'\d+', line) 
 
        print(temp)
        
        for i in range(int(temp[0]), int(temp[1])+1):
            elf1.append(i)
        for i in range(int(temp[2]), int(temp[3])+1):
            elf2.append(i)
        print(elf1)
        print(elf2)
        check =  all(item in elf1 for item in elf2)
        check1 =  all(item in elf2 for item in elf1)
 
        if check is True or check1 is True:
            print("The lists overlap")
            overlaps = overlaps + 1    
        else :
            print("No, the lists don't overlap.")
        elf1 = []
        elf2 = []
        temp = []

print ("There are: "  + str(overlaps) + " overlaps!")