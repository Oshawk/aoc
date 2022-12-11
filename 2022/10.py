instructions = []
with open("10.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("addx"):
            instructions.append("noop")

        instructions.append(line)

x = 1
signal_strengths = 0
crt = []
for i, instruction in enumerate(instructions):
    possibles = [j for j in range(x-1, x+2) if j < 40]
    if i % 40 in possibles:
        crt.append("#")
    else:
        crt.append(" ")

    if instruction.startswith("addx"):
        x += int(instruction.split()[1])
    elif instruction.startswith("noop"):
        pass

    # print(i, x)

    if i % 40 == 18:
        # print(i, x)
        signal_strengths += ((i + 2) * x)

print(signal_strengths)

print(crt)

buffer = []
for i in range(len(crt)):
    if i % 40 == 0:
        print("".join(buffer))
        buffer.clear()

    buffer.append(crt[i])

print("".join(buffer))
