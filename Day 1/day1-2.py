total = 0
calories = []

with open('input.txt', "r") as f:
    for line in f:
        line = line.rstrip('\r\n')
        if line.strip() == "":
            calories.append(total)
            total = 0
        else:
            total = int(line) + total
    calories.append(total)
    calories.sort()
    print(calories[-1] + calories[-2] + calories[-3])
