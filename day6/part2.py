text: str = ""

with open("input.txt") as file:
    text = file.read().strip()

for i in range(len(text)):
    if len(set(text[i-14:i])) == 14:
        print(i)
        break
