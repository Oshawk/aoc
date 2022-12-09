DIRECTIONS = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


class Rope:
    def __init__(self, length):
        self.positions = []
        for _ in range(length):
            self.positions.append((0, 0))

    def move(self, direction_x, direction_y):
        self.positions[0] = (self.positions[0][0] + direction_x, self.positions[0][1] + direction_y)

        for i in range(len(self.positions) - 1):
            head_x, head_y = self.positions[i]
            tail_x, tail_y = self.positions[i + 1]

            distance_x = head_x - tail_x
            distance_y = head_y - tail_y

            if abs(distance_x) <= 1 and abs(distance_y) <= 1:
                continue

            tail_x += 0 if distance_x == 0 else distance_x // abs(distance_x)
            tail_y += 0 if distance_y == 0 else distance_y // abs(distance_y)

            self.positions[i + 1] = (tail_x, tail_y)


def main():
    part_1 = {(0, 0)}
    part_2 = {(0, 0)}
    rope_1 = Rope(2)
    rope_2 = Rope(10)

    with open("9.txt") as f:
        for line in f.readlines():
            direction, amount = line.strip().split()
            direction_x, direction_y = DIRECTIONS[direction]
            amount = int(amount)

            for _ in range(amount):
                rope_1.move(direction_x, direction_y)
                rope_2.move(direction_x, direction_y)

                part_1.add(rope_1.positions[-1])
                part_2.add(rope_2.positions[-1])

    print(len(part_1))
    print(len(part_2))


if __name__ == '__main__':
    main()
