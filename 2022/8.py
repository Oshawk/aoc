def work(trees, visible, x, y, x_move, y_move, last=-1, restrict=None):
    if (x, y) not in visible:
        return

    if restrict is not None or trees[y][x] > last:
        visible[(x, y)] += 1

    if restrict is not None and trees[y][x] >= restrict:
        return

    work(trees, visible, x + x_move, y + y_move, x_move, y_move, last=max(last, trees[y][x]), restrict=restrict)


def make_visible(max_x, max_y):
    visible = {}
    for x in range(max_x):
        for y in range(max_y):
            visible[(x, y)] = 0

    return visible


def main():
    trees = []
    with open("8.txt") as f:
        for line in f.readlines():
            trees.append([int(tree) for tree in line.strip()])

    max_x = len(trees[0])
    max_y = len(trees)

    part_1 = make_visible(max_x, max_y)

    for x in range(max_x):
        work(trees, part_1, x, 0, 0, 1)
        work(trees, part_1, x, max_y - 1, 0, -1)

    for y in range(max_y):
        work(trees, part_1, 0, y, 1, 0)
        work(trees, part_1, max_x - 1, y, -1, 0)

    print(sum(1 for i in part_1.values() if i > 0))

    scenic_scores = {}
    for x in range(max_x):
        for y in range(max_y):
            scenic_score = 1
            for x_move, y_move in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                part_2 = make_visible(max_x, max_y)
                work(trees, part_2, x + x_move, y + y_move, x_move, y_move, restrict=trees[y][x])
                multiplier = sum(1 for i in part_2.values() if i > 0)
                scenic_score *= multiplier

            scenic_scores[(x, y)] = scenic_score

    print(max(scenic_scores.values()))


if __name__ == '__main__':
    main()
