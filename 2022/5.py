import re

stacks1 = []
stacks2 = []
with open("5.txt") as f:
    for line in f.readlines():
        if "[" in line:
            for i in range(1, len(line), 4):
                stack_index = (i - 1) // 4

                if len(stacks1) <= stack_index:
                    stacks1.append([])

                if len(stacks2) <= stack_index:
                    stacks2.append([])

                if line[i] != " ":
                    stacks1[stack_index].insert(0, line[i])
                    stacks2[stack_index].insert(0, line[i])
        elif match := re.findall(r"move (\d+) from (\d+) to (\d+)", line):
            count, from_, to = (int(i) for i in match[0])

            for _ in range(count):
                stacks1[to - 1].append(stacks1[from_ - 1].pop())

            stacks2[to - 1] += stacks2[from_ - 1][-count:]
            del stacks2[from_ - 1][-count:]


print("".join(stack[-1] for stack in stacks1))
print("".join(stack[-1] for stack in stacks2))
