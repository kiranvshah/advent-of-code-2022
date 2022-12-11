knot_coords = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
coords_tail_visited = set([0, 0])
instructions = []


with open("input.txt") as file:
    for line in file:
        instructions.append(line.split())


for instruction in instructions:
    direction = instruction[0]
    distance = int(instruction[1])
    for i in range(distance):
        if direction == "U":
            knot_coords[0][1] += 1
        elif direction == "D":
            knot_coords[0][1] -= 1
        elif direction == "L":
            knot_coords[0][0] -= 1
        elif direction == "R":
            knot_coords[0][0] += 1

        for trailing_knot_index in range(1, len(knot_coords)):
            trailing_knot = knot_coords[trailing_knot_index]
            leading_knot = knot_coords[trailing_knot_index - 1]

            if (
                abs(leading_knot[0] - trailing_knot[0]) > 1 or
                abs(leading_knot[1] - trailing_knot[1]) > 1
            ):
                if leading_knot[1] > trailing_knot[1]:
                    trailing_knot[1] += 1
                elif leading_knot[1] < trailing_knot[1]:
                    trailing_knot[1] -= 1
                if leading_knot[0] > trailing_knot[0]:
                    trailing_knot[0] += 1
                elif leading_knot[0] < trailing_knot[0]:
                    trailing_knot[0] -= 1

                if trailing_knot_index == len(knot_coords) - 1:
                    coords_tail_visited.add((trailing_knot[0], trailing_knot[1]))

print(len(coords_tail_visited))
