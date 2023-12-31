def parse_int(input: str) -> int:
    return int(input, 10)


def parse_lines(input: str) -> list[str]:
    return input.splitlines()


def parse_list(input: str) -> list[str]:
    return input.strip().split(",")


def parse_string(input: str) -> str:
    return str(input)
