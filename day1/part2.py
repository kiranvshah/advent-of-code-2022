with open("input.txt") as file:
    elves = [[int(line) for line in elf.split("\n")] for elf in file.read().split("\n\n")]

elves = [sum(elf) for elf in elves]
elves.sort()

print(sum(elves[-3:]))
