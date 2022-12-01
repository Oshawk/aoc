INPUT = open("1.txt").read()

elfs = []
for group in INPUT.split("\n\n"):
    elfs.append([])
    for calories in group.split():
        calories = int(calories)
        elfs[-1].append(calories)

print(max(sum(elf) for elf in elfs))

elfs.sort(key=lambda elf: sum(elf), reverse=True)

print(sum(sum(elf) for elf in elfs[:3]))
