with open("input.txt") as file:
    contents = file.read()
    crates = contents.split("\n\n")[0].split("\n")[:-1]
    instructions = [
        instruction.split(" ") for instruction in contents.split("\n\n")[1].strip().split("\n")
    ]
    instructions = [{
        "quantity": int(instruction[1]),
        "origin": int(instruction[3]),
        "destination": int(instruction[5])
    } for instruction in instructions]

rows = []
stacks = []

for crate in crates:
    rows.append(
        list(crate.replace("    ", "X").replace(" ", "").replace("[", "").replace("]",""))
    )

for i in range(len(rows[0])):
    stacks.append([row[i] for row in rows][::-1])

for stack in stacks:
    for i in range(len(stack)):
        if "X" in stack:
            stack.remove("X")

for instruction in instructions:
    quantity = instruction["quantity"]
    origin_index = instruction["origin"] - 1
    destination_index = instruction["destination"] - 1
    crates = stacks[origin_index][-quantity:]
    stacks[origin_index] = stacks[origin_index][:-quantity]
    stacks[destination_index] += crates

result: str = ""
for stack in stacks:
    result += stack[-1]
print(result)
