import re


def make_regex(number):
    regex = []
    for i in range(number):
        if i != 0:
            lookahead = "|".join(f"\\{j + 1}" for j in range(i))
            regex.append(f"(?!{lookahead})")

        regex.append("(.)")

    return "".join(regex)


with open("6.txt") as f:
    puzzle = f.read().strip()

print(re.search(make_regex(4), puzzle).span()[1])
print(re.search(make_regex(14), puzzle).span()[1])
