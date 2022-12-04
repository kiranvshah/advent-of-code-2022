rucksacks = []

with open("input.txt") as file:
    for line in file:
        rucksacks.append(line.strip())

print(rucksacks)
print(len(rucksacks))


ALPHABET = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(ALPHABET))

total = 0

for index in range(0, len(rucksacks), 3):
    r1 = rucksacks[index]
    r2 = rucksacks[index+1]
    r3 = rucksacks[index+2]
    for char in r1:
        if char in r3 and char in r2:
            total += ALPHABET.index(char)
            print(index, char, ALPHABET.index(char),total)
            break

print(total)
# print("g" in "RVnsmspnpwFRlHGRwHHlnRSThSSvBTbFTZMqTMZMTZFh")