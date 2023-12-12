from utilities.get_input import *
from utilities.parse import *
import time, re
from queue import Queue
from threading import Thread, Lock

class Day12:
    def __init__(self) -> None:
        self.input = get_input(2023, 12)
        self.parsed_input = parse_lines(self.input)
        self.springs_and_groups = self.parse_springs_and_groups()
        # Used for multithreading
        self.mutex = Lock()
        self.total_arrangements = 0
        return
    
    def parse_springs_and_groups(self) -> list[tuple[str, list[int]]]:
        springs_and_groups = []
        for line in self.parsed_input:
            springs, groups_input = line.split(' ')
            groups = [int(group) for group in groups_input.split(',')]
            springs_and_groups.append((springs, groups))
        return springs_and_groups
    
    def is_possibly_valid(self, arrangement: str, total_broken: int, groups: list[int]) -> bool:
        if arrangement.count('#') > total_broken:
            return False
        # Not enough "?" to convert to broken springs
        if arrangement.count('?') + arrangement.count('#') < total_broken:
            return False
        # No more "?"
        if arrangement.count('?') == 0:
            return False
        arrangement_upto_mystery = re.split(r'(#+\?)|\?', arrangement)[0]
        groups_of_broken_springs = [len(entry) for entry in re.findall(r'#+', arrangement_upto_mystery)]
        for i, group in enumerate(groups_of_broken_springs):
            if group != groups[i]:
                return False
        return True
    
    def is_valid(self, arrangement: str, groups: list[int]) -> bool:
        # No more "?" at all - check the arrangement is valid
        if arrangement.count('?') == 0:
            groups_of_broken_springs = [len(entry) for entry in re.findall(r"#+", arrangement)]
            if groups_of_broken_springs == groups:
                return True
        return False
    
    def check_arrangements(self, springs: str, groups: list[int]) -> None:
        start_time = time.time()
        arrangements_to_check: Queue[str] = Queue()
        arrangements_to_check.put(springs)
        total_broken = sum(groups)
        while arrangements_to_check.qsize() > 0:
                arrangement = arrangements_to_check.get()
                # Convert to working spring
                arrangement_working = arrangement.replace('?', '.', 1)
                if self.is_valid(arrangement_working, groups):
                    with self.mutex:
                        self.total_arrangements += 1
                    continue
                # Convert to broken spring
                arrangement_broken = arrangement.replace('?', '#', 1)
                if self.is_valid(arrangement_broken, groups):
                    with self.mutex:
                        self.total_arrangements += 1
                    continue
                if self.is_possibly_valid(arrangement_working, total_broken, groups):
                    arrangements_to_check.put(arrangement_working)
                if self.is_possibly_valid(arrangement_broken, total_broken, groups):
                    arrangements_to_check.put(arrangement_broken)
        print(f'Thread {springs}: {time.time() - start_time}')

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        self.total_arrangements = 0
        threads: list[Thread] = []
        for springs, groups in self.springs_and_groups:
            if part_2:
                springs = springs + '?' + springs + '?' + springs + '?' + springs + '?' + springs
                groups *= 5
            threads.append(Thread(target=self.check_arrangements, args=(springs, groups)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print(f'Part {'2' if part_2 else '1'}: {self.total_arrangements} - {time.time() - start_time}')


def main() -> None:
    day = Day12()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
