from utilities.get_input import *
from utilities.parse import *
import time, re, math
from typing import Callable

class Day8:
    def __init__(self) -> None:
        self.input = get_input(2023, 8).strip()
        self.instructions, self.lines  = self.input.split('\n\n')
        self.nodes = self.parse_nodes()
        return
    
    def parse_nodes(self) -> dict[str, tuple[str, str]]:
        nodes = {}
        for line in self.lines.split('\n'):
            node, left, right = re.findall(r'\w+', line)
            nodes[node] = (left, right)
        return nodes
    
    def count_steps(self, starting_node: str, check: Callable[[str], bool]) -> int:
        instruction = self.instructions[0]
        node = starting_node
        steps = 0
        while check(node):
            steps += 1
            left, right = self.nodes[node]
            node = right if instruction == 'R' else left
            instruction = self.instructions[steps % len(self.instructions)]
        return steps

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        count = 0
        if not part_2:
            node = 'AAA'
            count = self.count_steps(node, lambda node: node != 'ZZZ')
        else:
            nodes_ending_with_A = [node for node in self.nodes.keys() if node.endswith('A')]
            repeating = []
            for starting_node in nodes_ending_with_A:
                steps = self.count_steps(starting_node, lambda node: not node.endswith('Z'))
                repeating.append(steps)
            count = math.lcm(*repeating)
        print(f'Part {'2' if part_2 else '1'}: {count} - {time.time() - start_time}')


def main() -> None:
    day = Day8()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
