from utilities.get_input import *
from utilities.parse import *
import time, re
from utilities.Cube import Cube

test_input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

class Day22:
    def __init__(self) -> None:
        self.input = get_input(2023, 22)
        self.parsed_input = parse_lines(self.input)
        self.cubes = self.parse_cubes()
        return
    
    def parse_cubes(self) -> list[Cube]:
        cubes = []
        matcher = re.compile(r'\d+')
        for line in self.parsed_input:
            bottom_left_x, bottom_left_y, bottom_left_z, top_right_x, top_right_y, top_right_z =  matcher.findall(line)
            cubes.append(Cube(bottom_left_x, bottom_left_y, bottom_left_z, top_right_x, top_right_y, top_right_z))
        return cubes
    
    def sort_cubes(self) -> None:
        self.cubes.sort(key=lambda cube: cube.bottom_z)

    def cubes_below(self, cube: Cube) -> list[Cube]:
        cubes = []
        for other_cube in self.cubes:
            if cube.bottom_z > other_cube.top_z:
                cubes.append(other_cube)
        return cubes
    
    def cubes_directly_below(self, cube: Cube) -> list[Cube]:
        cubes = []
        for other_cube in self.cubes:
            if cube.bottom_z == other_cube.top_z + 1:
                cubes.append(other_cube)
        return cubes
    
    def cubes_directly_above(self, cube: Cube) -> list[Cube]:
        cubes = []
        for other_cube in self.cubes:
            if cube.top_z == other_cube.bottom_z - 1:
                cubes.append(other_cube)
        return cubes

    def cubes_overlap(self, cube: Cube, other: Cube) -> bool:
        return not (cube.top_x < other.bottom_x
                or cube.bottom_x > other.top_x
                or cube.top_y < other.bottom_y
                or cube.bottom_y > other.top_y)

    def move_cube_downwards(self, cube: Cube) -> None:
        cubes_below = self.cubes_below(cube)
        while True:
            can_move_down = True
            for other_cube in cubes_below:
                if self.cubes_overlap(cube, other_cube) and cube.bottom_z - 1 <= other_cube.top_z:
                    can_move_down &= False
            if can_move_down and cube.bottom_z > 1:
                cube.bottom_z -= 1
                cube.top_z -= 1
            else:
                break

    def supports(self, cube: Cube) -> list[Cube]:
        cubes_above = self.cubes_directly_above(cube)
        supports = []
        for other_cube in cubes_above:
            if self.cubes_overlap(cube, other_cube):
                supports.append(other_cube)
        return supports

    def supported_by(self, cube: Cube) -> list[Cube]:
        cubes_below = self.cubes_directly_below(cube)
        supported_by = []
        for other_cube in cubes_below:
            if self.cubes_overlap(cube, other_cube):
                supported_by.append(other_cube)
        return supported_by

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        self.sort_cubes()
        for cube in self.cubes:
            self.move_cube_downwards(cube)
        supports = dict()
        supported_by = dict()
        can_disintegrate = set()
        for cube in self.cubes:
            supports[cube] = self.supports(cube)
            supported_by[cube] = self.supported_by(support)
        for cube in self.cubes:
            if len(supports.get(cube)) == 0:
                can_disintegrate.add(cube)
            else:
                for support in supports.get(cube):
                    if len(supported_by.get(support)) > 1:
                        can_disintegrate.add(cube)
        print(f'Part {'2' if part_2 else '1'}: {len(can_disintegrate)} - {time.time() - start_time}')


def main() -> None:
    day = Day22()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
