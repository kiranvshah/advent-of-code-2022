pairs = []

with open("input.txt") as file:
    for line in file:
        pairs.append([[int(num) for num in elf.split("-")] for elf in line.strip().split(",")])

total_overlapping = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
        total_overlapping += 1

print(total_overlapping)