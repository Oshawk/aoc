from typing import Optional, Generator


class Directory:
    parent: Optional["Directory"]
    directories: dict[str, "Directory"]
    files: dict[str, int]

    def __init__(self, parent: Optional["Directory"]):
        self.parent = parent
        self.directories = {}
        self.files = {}

    def add_directory(self, name: str, directory: "Directory") -> None:
        if name not in self.directories:
            self.directories[name] = directory

    def add_file(self, name: str, size: int) -> None:
        if name not in self.files:
            self.files[name] = size

    def solve(self) -> Generator[int, None, int]:
        sum_ = 0

        for size in self.files.values():
            sum_ += size

        for directory in self.directories.values():
            sum_ += yield from directory.solve()

        yield sum_
        return sum_


def main() -> None:
    root = None
    directory = None
    with open("7.txt") as f:
        for line in f.readlines():
            line = line.strip()

            if line.startswith("$ cd"):
                name = line.split()[2]

                if name == "..":
                    directory = directory.parent
                else:
                    if directory is None:
                        assert name == "/"
                        root = Directory(None)
                        directory = root
                    else:
                        directory = directory.directories[name]
            elif line == "$ ls":
                pass
            else:
                size, name = line.split()

                if size == "dir":
                    directory.add_directory(name, Directory(directory))
                else:
                    size = int(size)
                    directory.add_file(name, size)

    sums = [sum_ for sum_ in root.solve()]
    print(sum(sum_ for sum_ in sums if sum_ <= 100000))

    size_needed = 30000000 - (70000000 - sums[-1])
    print(min(sum_ for sum_ in sums if sum_ >= size_needed))


if __name__ == '__main__':
    main()