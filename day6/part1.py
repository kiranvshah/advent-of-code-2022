text: str = ""

with open("input.txt") as file:
    text = file.read().strip()

for i in range(len(text)):
    if len(set(text[i-4:i])) == 4:
        print(i)
        break
