from random import choice, randint
from string import ascii_letters, digits

from tqdm import tqdm

CHARACTER_SET = ascii_letters + digits

WINDOW_SIZE = 60
LENGTH = 100_000_000

result = []
for _ in range(WINDOW_SIZE):
    while (character := choice(CHARACTER_SET)) in result:
        pass

    result.append(character)

insertion_point = randint(0, LENGTH-WINDOW_SIZE)
for _ in tqdm(range(insertion_point-WINDOW_SIZE)):
    while (character := choice(CHARACTER_SET)) not in result[:WINDOW_SIZE]:
        pass

    result.insert(0, character)

for _ in tqdm(range(LENGTH-insertion_point)):
    result.append(choice(CHARACTER_SET))

with open("6_long.txt", "w") as f:
    f.write("".join(result))
