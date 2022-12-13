instructions = []
cycles_completed: int = 0
sprite_horizontal_position: int = 1
crt_display_data = []

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line == "noop":
            instructions.append("noop")
        else:
            instructions.append("noop") # first cycle
            instructions.append(int(line.split()[1])) # second cycle - add

for instruction in instructions:
    print(sprite_horizontal_position, cycles_completed)
    if abs(sprite_horizontal_position - (cycles_completed % 40)) <= 1:
        crt_display_data.append("#")
    else:
        crt_display_data.append(".")
    if instruction == "noop":
        pass
    else:
        sprite_horizontal_position += instruction
    cycles_completed += 1

# print crt
while crt_display_data:
    for i in range(40):
        print(crt_display_data[0], end="")
        crt_display_data.pop(0)
    print("")
