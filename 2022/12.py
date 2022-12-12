import sys


def search(grid: list[list[str]], visited: tuple[tuple[int, int], ...], best_at_position: dict[tuple[int, int], int], current_x: int, current_y: int, end_x: int, end_y: int) -> None:
    visited += ((current_x, current_y),)

    if (current_x, current_y) not in best_at_position or len(visited) < best_at_position[(current_x, current_y)]:
        best_at_position[(current_x, current_y)] = len(visited)
    else:
        return

    if current_x == end_x and current_y == end_y:
        return

    current_character = grid[current_y][current_x]

    possibles = []
    for delta_x, delta_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= (current_x + delta_x) < len(grid[0]) and 0 <= (current_y + delta_y) < len(grid) and (current_x + delta_x, current_y + delta_y) not in visited and ord(current_character) + 1 >= ord(grid[current_y + delta_y][current_x + delta_x]):
            possibles.append((current_x + delta_x, current_y + delta_y))

    possibles.sort(key=lambda possible: abs(end_x - possible[0]) + abs(end_y - possible[1]) + (ord(current_character) - ord(grid[possible[1]][possible[0]])))

    for possible in possibles:
        search(grid, visited, best_at_position, possible[0], possible[1], end_x, end_y)


def main():
    grid = []
    start_x, start_y = None, None
    end_x, end_y = None, None
    with open("12.txt") as f:
        for line in f.readlines():
            row = []
            line = line.strip()
            for character in line:
                if character == "S":
                    start_x = len(row)
                    start_y = len(grid)
                    row.append("a")
                elif character == "E":
                    end_x = len(row)
                    end_y = len(grid)
                    row.append("z")
                else:
                    row.append(character)

            grid.append(row)

    assert all(i is not None for i in (start_x, start_y, end_x, end_y))

    best_at_position = {}
    sys.setrecursionlimit(10000)
    search(grid, tuple(), best_at_position, start_x, start_y, end_x, end_y)
    print(best_at_position[(end_x, end_y)] - 1)

    start_positions = []
    for y, row in enumerate(grid):
        for x, character in enumerate(row):
            if character == "a":
                start_positions.append((x, y))

    start_positions.sort(key=lambda start_position: abs(start_position[0] - end_x) + abs(start_position[1] - end_y))

    for start_position in start_positions:
        search(grid, tuple(), best_at_position, start_position[0], start_position[1], end_x, end_y)

    print(best_at_position[(end_x, end_y)] - 1)


if __name__ == '__main__':
    main()
