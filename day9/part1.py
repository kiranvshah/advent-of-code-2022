head_coords = [0, 0]
tail_coords = [0, 0]
coords_tails_visited = set(tail_coords.copy())
instructions = []


with open("input.txt") as file:
    for line in file:
        instructions.append(line.split())


for instruction in instructions:
    direction = instruction[0]
    distance = int(instruction[1])
    for i in range(distance):
        if direction == "U":
            head_coords[1] += 1
        elif direction == "D":
            head_coords[1] -= 1
        elif direction == "L":
            head_coords[0] -= 1
        elif direction == "R":
            head_coords[0] += 1

        if abs(head_coords[0] - tail_coords[0]) > 1 or abs(head_coords[1] - tail_coords[1]) > 1:
            if head_coords[1] > tail_coords[1]:
                tail_coords[1] += 1
            elif head_coords[1] < tail_coords[1]:
                tail_coords[1] -= 1
            if head_coords[0] > tail_coords[0]:
                tail_coords[0] += 1
            elif head_coords[0] < tail_coords[0]:
                tail_coords[0] -= 1
            coords_tails_visited.add((tail_coords[0], tail_coords[1]))

print(len(coords_tails_visited))
