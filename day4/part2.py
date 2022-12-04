pairs = []

with open("input.txt") as file:
    for line in file:
        pairs.append([[int(num) for num in elf.split("-")] for elf in line.strip().split(",")])

total_overlapping = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    elf1nums = set(range(elf1[0], elf1[1]+1))
    elf2nums = set(range(elf2[0], elf2[1]+1))
    if elf1nums.intersection(elf2nums):
        total_overlapping += 1

print(total_overlapping)