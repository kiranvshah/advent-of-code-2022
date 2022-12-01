with open("input.txt") as file:
    elves = [[int(line) for line in elf.split("\n")] for elf in file.read().split("\n\n")]

largest_elf_score: int = 0
for elf in elves:
    if sum(elf) > largest_elf_score:
        largest_elf_score = sum(elf)
print(largest_elf_score)
