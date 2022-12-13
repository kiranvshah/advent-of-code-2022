instructions = []
cycles_completed: int = 0
x: int = 1
signal_strengths_total: int = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line == "noop":
            instructions.append("noop")
        else:
            instructions.append("noop") # first cycle
            instructions.append(int(line.split()[1])) # second cycle - add

for instruction in instructions:
    if cycles_completed in [19, 59, 99, 139, 179, 219]:
        SIGNAL_STRENGTH = (cycles_completed + 1) * x
        signal_strengths_total += SIGNAL_STRENGTH
    if instruction == "noop":
        pass
    else:
        x += instruction
    cycles_completed += 1

print(signal_strengths_total)
