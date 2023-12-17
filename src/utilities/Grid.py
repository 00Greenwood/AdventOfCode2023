class Grid:
    def __init__(self, input: str = None, as_int: bool = False) -> None:
        self.grid: dict = {}
        if input:
            for y, line in enumerate(input.splitlines()):
                for x, char in enumerate(line):
                    self.grid[f"{x}, {y}"] = char if not as_int else int(char)
        self.max_x = max(self.keys(), key=lambda x: x[0])[0]
        self.max_y = max(self.keys(), key=lambda x: x[1])[1]

    def get(self, x: int, y: int):
        return self.grid.get(f"{x}, {y}")

    def get_row(self, y: int) -> list:
        return [self.grid.get(f"{x}, {y}") for x in range(self.size()[0])]

    def get_column(self, x: int) -> list:
        return [self.grid.get(f"{x}, {y}") for y in range(self.size()[1])]

    def set(self, x: int, y: int, char) -> None:
        self.grid[f"{x}, {y}"] = char

    def max(self) -> tuple[int, int]:
        return (self.max_x, self.max_y)

    def size(self) -> tuple[int, int]:
        x, y = self.max()
        return (x + 1, y + 1)

    def keys(self) -> list[tuple[int, int]]:
        keys: list[tuple[int, int]] = []
        for k, v in self.grid.items():
            x, y = k.split(", ")
            keys.append((int(x), int(y)))
        return keys

    def find(self, char) -> tuple[int, int]:
        for k, v in self.grid.items():
            if v == char:
                x, y = k.split(", ")
                return (int(x), int(y))

    def find_all(self, char) -> list[tuple[int, int]]:
        output: list[tuple[int, int]] = []
        for k, v in self.grid.items():
            if v == char:
                x, y = k.split(", ")
                output.append((int(x), int(y)))
        return output

    def print(self, separator: str) -> None:
        for y in range(self.size()[1]):
            print(separator.join(self.get_row(y)))
        print()
        return
