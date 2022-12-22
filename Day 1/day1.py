total = 0
with open('input.txt', 'r', encoding="utf-8") as f, open('newinput.txt', 'w') as o:
    lines = f.readlines()

    for line in lines:
        if line.strip() == "":
            print('The line is empty')
            o.write(",\n")
            total = 0
        else:
            print('The line is NOT empty', line)
            total = total + int(line)
            o.write(line)

#print(total)