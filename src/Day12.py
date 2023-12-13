from utilities.get_input import *
from utilities.parse import *
import time, re
from functools import cache

class Day12:
    def __init__(self) -> None:
        self.input = get_input(2023, 12)
        self.parsed_input = parse_lines(self.input)
        self.springs_and_groupings = self.parse_springs_and_groupings()
        return
    
    def parse_springs_and_groupings(self) -> list:
        springs_and_groupings = []
        for line in self.parsed_input:
            springs, groupings_input = line.split(' ')
            groupings = tuple([int(group) for group in groupings_input.split(',')])
            springs_and_groupings.append((springs, groupings))
        return springs_and_groupings

    working_springs_matcher = re.compile(r'\.+')

    @cache
    def get_broken_springs_matcher(i: int) -> re.Pattern:
        # Finds the next `i` broken and possible broken springs followed by a working spring or a possible working spring
        return re.compile(r"[\#\?]{%i}(\.|\?|$)" % i)

    @cache
    def count_arrangements(springs: str, groupings: tuple) -> int:
        if len(springs) == 0:
            if len(groupings) > 0:
                return 0 # Arrangement not found
            return 1 # Arrangement found
        
        if len(groupings) == 0:
            if '#' in springs:
                return 0 # There are leftover broken springs not in a group
            return 1 # All groupings assigned
        
        # Remove all working springs from the start and continue
        working_springs = Day12.working_springs_matcher.match(springs)
        if working_springs:
            number_of_working_springs = len(working_springs.group())
            return Day12.count_arrangements(springs[number_of_working_springs:], groupings)
        
        arrangements = 0

        # Check the case where the '?' is actually a working spring, i.e. remove it and continue
        if springs[0] == '?':
            arrangements += Day12.count_arrangements(springs[1:], groupings)

        # Check the case where the '?' is actually a broken spring, i.e. remove the next number of broken springs and continue
        broken_springs = Day12.get_broken_springs_matcher(groupings[0]).match(springs)
        if broken_springs:
            number_of_broken_springs = len(broken_springs.group())
            arrangements += Day12.count_arrangements(springs[number_of_broken_springs:], groupings[1:])

        return arrangements

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        total_arrangements = 0
        for springs, groupings in self.springs_and_groupings:
            if part_2:
                springs = springs + '?' + springs + '?' + springs + '?' + springs + '?' + springs
                groupings *= 5
            total_arrangements += Day12.count_arrangements(springs, groupings)
        print(f'Part {'2' if part_2 else '1'}: {total_arrangements} - {time.time() - start_time}')


def main() -> None:
    day = Day12()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
