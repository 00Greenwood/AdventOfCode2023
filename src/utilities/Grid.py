class Grid:
    def __init__(self, input: str) -> None:
        self.grid: dict[str, str] = {}
        for y, line in enumerate(input.splitlines()):
            for x, char in enumerate(line):
                self.grid[f"{x}, {y}"] = char

    def get(self, x: int, y: int) -> str:
        return self.grid.get(f"{x}, {y}")

    def set(self, x: int, y: int, char: str) -> None:
        self.grid[f"{x}, {y}"] = char

    def size(self) -> tuple[int, int]:
        x = max(self.keys(), key=lambda x: x[0])[0]
        y = max(self.keys(), key=lambda x: x[1])[1]
        return (x, y)

    def keys(self) -> list[tuple[int, int]]:
        keys: list[tuple[int, int]] = []
        for k, v in self.grid.items():
            x, y = k.split(", ")
            keys.append((int(x), int(y)))
        return keys

    def find(self, char: str) -> tuple[int, int]:
        for k, v in self.grid.items():
            if v == char:
                x, y = k.split(", ")
                return (int(x), int(y))
