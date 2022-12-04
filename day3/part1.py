rucksacks = []

with open("input.txt") as file:
    for line in file:
        rucksacks.append([line.strip()[:len(line)//2], line.strip()[len(line)//2:]])

print(rucksacks)

ALPHABET = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

for rucksack in rucksacks:
    charsDone = []
    for char in rucksack[0]:
        if char in rucksack[1] and char not in charsDone:
            total += ALPHABET.index(char)
            print(char, ALPHABET.index(char))
            charsDone.append(char)

print(total)