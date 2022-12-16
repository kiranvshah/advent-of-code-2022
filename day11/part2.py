from math import lcm

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

factors = [monkey["test"]["divisible_by"] for monkey in monkeys]
lowest_common_multiple = lcm(*factors)

for i in range(10_000):
    for monkey in monkeys:
        QUANTITY = monkey["operation"]["quantity"]
        if monkey["operation"]["operation"] == "*":
            if QUANTITY == "old":
                monkey["items"] = [item * item for item in monkey["items"]]
            else:
                monkey["items"] = [
                    item * QUANTITY for item in monkey["items"]
                ]
        else:
            if QUANTITY == "old":
                monkey["items"] = [item + item for item in monkey["items"]]
            else:
                monkey["items"] = [
                    item + QUANTITY for item in monkey["items"]
                ]
        for item in monkey["items"]:
            item  %= lowest_common_multiple
            if item % monkey["test"]["divisible_by"] == 0:
                monkeys[monkey["test"]["throw_if_true"]]["items"].append(item)
            else:
                monkeys[monkey["test"]["throw_if_false"]]["items"].append(item)
            monkey["inspected"] += 1
        monkey["items"] = []

inspected_counts = [monkey["inspected"] for monkey in monkeys]
inspected_counts.sort()
print(inspected_counts[-1] * inspected_counts[-2])
