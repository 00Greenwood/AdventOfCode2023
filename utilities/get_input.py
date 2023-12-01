import os, requests


def get_input(year: int, day: int) -> str:
    session = os.getenv("AOC_SESSION")
    if session is None:
        raise Exception("AOC_SESSION environment variable not set")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(url, cookies={"session": session})
    if response.status_code is not 200:
        raise Exception(f"Error fetching input: {response.status_code}")
    return response.text


if __name__ == "__main__":
    print(get_input(2022, 24))
