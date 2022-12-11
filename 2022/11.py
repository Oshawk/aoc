from math import lcm
from typing import Generator

from tqdm import tqdm


class Monkey:
    items: list[int]
    operation: str
    test: int
    test_true: int
    test_false: int
    inspected_count: int

    def __init__(self, items: list[int], operation: str, test: int, test_true: int, test_false: int) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspected_count = 0

    def round(self, divisor=3, modulus=None) -> Generator[int, None, None]:
        for i in range(len(self.items)):
            self.items[i] = eval(self.operation.replace("old", str(self.items[i]))) // divisor

            if modulus is not None:
                self.items[i] %= modulus

            self.inspected_count += 1

        while True:
            try:
                item = self.items.pop(0)
                if item % self.test == 0:
                    yield self.test_true, item
                else:
                    yield self.test_false, item
            except IndexError:
                return


def main() -> None:
    with open("11.txt") as f:
        lines = [i.strip() for i in f.readlines()]

    monkeys_1 = []
    monkeys_2 = []
    while True:
        try:
            lines.pop(0)
            starting_items = [int(i) for i in lines.pop(0).split(": ")[1].split(", ")]
            operation = lines.pop(0).split("new = ")[1]
            test = int(lines.pop(0).split("by ")[1])
            test_true = int(lines.pop(0).split("monkey ")[1])
            test_false = int(lines.pop(0).split("monkey ")[1])
            monkeys_1.append(Monkey(starting_items, operation, test, test_true, test_false))
            monkeys_2.append(Monkey(starting_items.copy(), operation, test, test_true, test_false))
            lines.pop(0)
        except IndexError:
            break

    modulus = lcm(*[monkey.test for monkey in monkeys_2])

    for _ in range(20):
        for from_monkey in monkeys_1:
            for to_monkey, item in from_monkey.round():
                monkeys_1[to_monkey].items.append(item)

    for _ in tqdm(range(10000)):
        for from_monkey in monkeys_2:
            for to_monkey, item in from_monkey.round(divisor=1, modulus=modulus):
                monkeys_2[to_monkey].items.append(item)

    inspected_counts_1 = [monkey.inspected_count for monkey in monkeys_1]
    inspected_counts_1.sort(reverse=True)
    print(inspected_counts_1[0] * inspected_counts_1[1])

    inspected_counts_2 = [monkey.inspected_count for monkey in monkeys_2]
    inspected_counts_2.sort(reverse=True)
    print(inspected_counts_2[0] * inspected_counts_2[1])


if __name__ == '__main__':
    main()
