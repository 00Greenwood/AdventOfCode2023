from utilities.get_input import *
from utilities.parse import *
import time, re, math


type Part = dict[str, int]
type PartRange = tuple[int, int]
type PartRanges = dict[str, PartRange]
type Rules = list[tuple(str, str | None, int | None, str | None)]

class Day19:
    def __init__(self) -> None:
        self.input = get_input(2023, 19)
        self.parsed_input = self.input.strip().split('\n\n')
        self.rules = self.parse_rules(self.parsed_input[0])
        self.parts = self.parse_parts(self.parsed_input[1])
        return
    
    def parse_rules(self, input: str) -> None:
        set_of_rules: dict[str, Rules] = dict()
        for line in input.split('\n'):
            id, rules_input = line.split('{')
            set_of_rules[id] = list()
            for rule in rules_input[:-1].split(','):
                if rule.count(':') > 0:
                    predicate, next_rule = rule.split(':')
                    if predicate.count('>') > 0:
                        part_id, value = predicate.split('>')
                        set_of_rules[id].append((next_rule, part_id, int(value), '>'))
                    else:
                        part_id, value = predicate.split('<')
                        set_of_rules[id].append((next_rule, part_id, int(value), '<'))
                else: # Default rule
                    set_of_rules[id].append((rule, None, None, None))
        return set_of_rules

    def parse_parts(self, input: str) -> list[Part]:
        matcher = re.compile(r'\d+')
        parts: list[Part] = []
        for line in input.split('\n'):
            x, m, a, s = matcher.findall(line)
            parts.append({'x': int(x), 'm':int(m), 'a':int(a), 's':int(s)})
        return parts
            
    def check_part(self, part: Part, rules: Rules) -> str:
        for rule, part_id, value, operation in rules:
            if operation is None: # Default rule
                if rule == 'A' or rule == 'R':
                    return rule
                return self.check_part(part, self.rules[rule])
            elif operation == '>':
                next_rule = rule if part[part_id] > value else None
            else:
                next_rule = rule if part[part_id] < value else None
            if next_rule is None:
                continue
            if next_rule == 'A' or next_rule == 'R':
                return next_rule
            return self.check_part(part, self.rules[next_rule])
        raise Exception('No rule matched')
    
    def check_rule(self, rule: str, part_ranges: PartRanges) -> int:
        if rule == 'A':
            valid_parts: list[int] = list()
            for _, value in part_ranges.items():
                valid_parts.append(value[1] - value[0] + 1) # Inclusive!
            return math.prod(valid_parts)
        elif rule == 'R':
            return 0 # All parts in this range are rejected!
        else :
            return self.check_range(part_ranges, self.rules[rule])

    def check_range(self, part_ranges: PartRanges, rules: Rules) -> int:
        valid_parts = 0
        for rule, part_id, value, operation in rules:
            if operation is None: # Default rule
                return valid_parts + self.check_rule(rule, part_ranges)
            part_range = part_ranges[part_id]
            valid_part_range: PartRange | None = None
            invalid_part_range: PartRange | None = None
            if operation == '>':
                # Check for any overlapping part ranges
                if part_range[0] > value: # Range is completely above value
                    valid_part_range = part_range
                elif part_range[1] <= value: # Range is completely below value
                    invalid_part_range = part_range
                elif part_range[0] <= value and part_range[1] > value: # Range is overlapping value
                    invalid_part_range = (part_range[0], value)
                    valid_part_range = (value + 1, part_range[1])
            else:
                # Check for any overlapping part ranges
                if part_range[1] < value: # Range is completely above value
                    valid_part_range = part_range
                elif part_range[0] >= value: # Range is completely below value
                    invalid_part_range = part_range
                elif part_range[0] < value and part_range[1] >= value: # Range is overlapping value
                    valid_part_range = (part_range[0], value - 1)
                    invalid_part_range = (value, part_range[1])
            if valid_part_range is not None:
                new_part_ranges = part_ranges.copy()
                new_part_ranges[part_id] = valid_part_range
                valid_parts += self.check_rule(rule, new_part_ranges)
            if invalid_part_range is not None:
                part_ranges[part_id] = invalid_part_range
        return valid_parts
            

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        rating = 0
        if not part_2:
            for part in self.parts:
                if self.check_part(part, self.rules['in']) == 'A':
                    for _, value in part.items():
                        rating += value
        else:
            rating = self.check_range({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, self.rules['in'])
        print(f'Part {'2' if part_2 else '1'}: {rating} - {time.time() - start_time}')


def main() -> None:
    day = Day19()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
