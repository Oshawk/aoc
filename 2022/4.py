import re

s1 = 0
s2 = 0
with open("4.txt") as f:
    for line in f.readlines():
        line = line.strip()

        a1, a2, b1, b2 = (int(i) for i in re.split(r"[,-]", line))

        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
            s1 += 1

        if a1 <= b2 and b1 <= a2:
            s2 += 1

print(s1)
print(s2)
