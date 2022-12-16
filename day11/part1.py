monkeys = []

with open("input.txt") as file:
    for monkey_data in file.read().split("\n\n"):
        lines = [line.strip().split() for line in monkey_data.split("\n")]
        monkeys.append({
            "items": [int(item.replace(",", "")) for item in lines[1][2:]],
            "operation": {
                "operation": lines[2][-2],
                "quantity": int(lines[2][-1]) if lines[2][-1].isdigit() else "old"
            },
            "test": {
                "divisible_by": int(lines[3][-1]),
                "throw_if_true": int(lines[4][-1]),
                "throw_if_false": int(lines[5][-1]),
            },
            "inspected": 0
        })

for i in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            if monkey["operation"]["operation"] == "*":
                if monkey["operation"]["quantity"] == "old":
                    item *= item
                else:
                    item *= monkey["operation"]["quantity"]
            else:
                if monkey["operation"]["quantity"] == "old":
                    item += item
                else:
                    item += monkey["operation"]["quantity"]
            item //= 3
            if item % monkey["test"]["divisible_by"] == 0:
                monkeys[monkey["test"]["throw_if_true"]]["items"].append(item)
            else:
                monkeys[monkey["test"]["throw_if_false"]]["items"].append(item)
            monkey["inspected"] += 1
        monkey["items"] = []

inspected_counts = [monkey["inspected"] for monkey in monkeys]
inspected_counts.sort()
print(inspected_counts[-1] * inspected_counts[-2])
