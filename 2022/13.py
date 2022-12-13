def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right

    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    i = 0
    while True:
        if i >= len(left) and i >= len(right):
            return None

        if i >= len(left):
            return True

        if i >= len(right):
            return False

        result = compare(left[i], right[i])
        if result is not None:
            return result

        i += 1


class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __lt__(self, other):
        return compare(self.packet, other.packet)


def main():
    sum_valid_i = 0
    all_packets = []
    with open("13.txt") as f:
        i = 0
        while (left := f.readline().strip()) != "":
            left = eval(left)
            right = eval(f.readline().strip())

            all_packets.append(Packet(left))
            all_packets.append(Packet(right))

            if compare(left, right):
                sum_valid_i += i + 1

            f.readline()
            i += 1

    print(sum_valid_i)

    divider_1 = Packet([[2]])
    divider_2 = Packet([[6]])
    all_packets.append(divider_1)
    all_packets.append(divider_2)

    all_packets.sort()

    print((all_packets.index(divider_1) + 1) * (all_packets.index(divider_2) + 1))


if __name__ == '__main__':
    main()
