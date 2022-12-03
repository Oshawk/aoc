def priority(item):
    item = ord(item)

    if ord("a") <= item <= ord("z"):
        return item - ord("a") + 1
    elif ord("A") <= item <= ord("Z"):
        return item - ord("A") + 27


s1 = 0
s2 = 0

with open("3.txt") as f:
    group = []
    for line in f.readlines():
        line = line.strip()

        group.append(set(line))

        compartment_1 = line[:len(line)//2]
        compartment_2 = line[len(line)//2:]

        for i in set(compartment_1) & set(compartment_2):
            s1 += priority(i)

        if len(group) == 3:
            badge = group[0] & group[1] & group[2]

            assert len(badge) == 1

            for i in badge:
                s2 += priority(i)

            group.clear()

print(s1)
print(s2)
