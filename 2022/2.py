from enum import IntEnum


class Choice(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


CHOICES = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS
}

OFFSETS = {
    "X": -1,
    "Y": 0,
    "Z": 1
}


CHOICE_SCORES = {
    Choice.ROCK: 1,
    Choice.PAPER: 2,
    Choice.SCISSORS: 3
}

LOSE = 0
DRAW = 3
WIN = 6


def get_score(their_choice, my_choice):
    score = CHOICE_SCORES[my_choice]

    if their_choice == (my_choice + 1) % 3:
        score += LOSE
    elif their_choice == my_choice:
        score += DRAW
    else:
        score += WIN

    return score


def main():
    score_1 = 0
    score_2 = 0
    with open("2.txt") as f:
        for line in f.readlines():
            their_choice, my_choice = line.split()

            their_choice = CHOICES[their_choice]

            score_1 += get_score(their_choice, CHOICES[my_choice])
            score_2 += get_score(their_choice, Choice((their_choice + OFFSETS[my_choice]) % 3))

    print(score_1)
    print(score_2)


if __name__ == '__main__':
    main()
