def main():
    grid = {}
    with open("14.txt") as f:
        for line in f.readlines():
            path = [tuple(int(coordinate) for coordinate in point.split(",")) for point in line.strip().split(" -> ")]

            last_point = path[0]
            for point in path[1:]:
                for x in range(min(point[0], last_point[0]), max(point[0], last_point[0]) + 1):
                    for y in range(min(point[1], last_point[1]), max(point[1], last_point[1]) + 1):
                        grid[(x, y)] = "#"

                last_point = point

    max_y = max(point[1] for point in grid.keys())

    sands = 0
    part_1 = None
    part_2 = None
    while True:
        sands += 1
        sand_x = 500
        sand_y = 0
        while True:
            if (sand_x, sand_y + 1) not in grid and (sand_y + 1) != max_y + 2:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in grid and (sand_y + 1) != max_y + 2:
                sand_x -= 1
                sand_y += 1
            elif (sand_x + 1, sand_y + 1) not in grid and (sand_y + 1) != max_y + 2:
                sand_x += 1
                sand_y += 1
            else:
                if sand_y == 0:
                    part_2 = sands
                    
                break

            if sand_y > max_y and part_1 is None:
                part_1 = sands - 1

        grid[(sand_x, sand_y)] = "o"

        if part_2 is not None:
            break

    print(part_1)
    print(part_2)


if __name__ == '__main__':
    main()
