import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="generate", description="generates a template Day file"
    )
    parser.add_argument("-d", "--day", type=int)
    args = parser.parse_args()
    createFile(args.day)
    return


def createFile(day: int) -> None:
    template: str
    with open(f"src/Day0.py", "r") as f:
        template = f.read()
    template = template.replace("Day0", f"Day{day}")
    with open(f"src/Day{day}.py", "x") as f:
        f.write(template)
    return


if __name__ == "__main__":
    main()
