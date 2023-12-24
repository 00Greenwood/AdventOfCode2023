from utilities.get_input import *
from utilities.parse import *
import time, re
from sympy import solve
from sympy.abc import x, y, z, a, b, c, r, s, t

Position = tuple[float, float, float]
Velocity = tuple[float, float, float]
Hail = tuple[Position, Velocity]

class Day24:
    def __init__(self) -> None:
        self.input = get_input(2023, 24)
        self.parsed_input = parse_lines(self.input)
        self.hails = self.parse_hails()
        return
    
    def parse_hails(self) -> list[Hail]:
        hails = []
        separator = re.compile(r'-?\d+')
        for line in self.parsed_input:
            px, py, pz, vx, vy, vz = separator.findall(line)
            hails.append(((float(px), float(py), float(pz)), (float(vx), float(vy), float(vz))))
        return hails
    
    def intersect(self, hail: Hail, other_hail: Hail) -> Position | None:
        # We want to solve:
        # x0 + dx0 * t = x1 + dx1 * s
        # y0 + dy0 * t = y1 + dy1 * s
        x_0, y_0, z_0 = hail[0]
        dx_0, dy_0, dz_0 = hail[1]
        x_1, y_1, z_1 = other_hail[0]
        dx_1, dy_1, dz_1 = other_hail[1]
        solutions = solve([x_0 + dx_0 * t - x_1 - dx_1 * s, y_0 + dy_0 * t - y_1 - dy_1 * s], [s,t], dict=True)
        if len(solutions) == 0 or solutions[0][s] < 0 or solutions[0][t] < 0:
            return None # Solution is in the past
        return (x_0 + dx_0 * solutions[0][t], y_0 + dy_0 * solutions[0][t], z_0 + dz_0 * solutions[0][t])

    def find_intersecting_line(self, hails: list[Hail]) -> tuple[Position, Velocity]:
        # Assume our rock will have position (x, y, z) and velocity (a, b, c)
        # We want to solve:
        # x0 + dx0 * t = x + a * t
        # y0 + dy0 * t = y + b * t
        # z0 + dz0 * t = z + c * t
        # x1 + dx1 * s = x + a * s
        # y1 + dy1 * s = y + b * s
        # z1 + dz1 * s = z + c * s
        # x2 + dx2 * r = x + a * r
        # y2 + dy2 * r = y + b * r
        # z2 + dz2 * r = z + c * r
        x_0, y_0, z_0 = hails[0][0]
        dx_0, dy_0, dz_0 = hails[0][1]
        x_1, y_1, z_1 =  hails[1][0]
        dx_1, dy_1, dz_1 =  hails[1][1]
        x_2, y_2, z_2 =  hails[2][0]
        dx_2, dy_2, dz_2 =  hails[2][1]    
        solutions = solve([
            x_0 - x + (dx_0 - a) * t,
            y_0 - y + (dy_0 - b) * t,
            z_0 - z + (dz_0 - c) * t,
            x_1 - x + (dx_1 - a) * s,
            y_1 - y + (dy_1 - b) * s,
            z_1 - z + (dz_1 - c) * s,
            x_2 - x + (dx_2 - a) * r,
            y_2 - y + (dy_2 - b) * r,
            z_2 - z + (dz_2 - c) * r
        ], [x, y, z, a, b, c, r, s, t], dict=True)
        return ((solutions[0][x], solutions[0][y], solutions[0][z]), (solutions[0][a], solutions[0][b], solutions[0][c]))
        

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        output = 0
        if not part_2:
            bounding_box = (200000000000000, 400000000000000)
            intersections_inside = []
            for i in range(len(self.hails)):
                for j in range(i + 1, len(self.hails)):
                    intersection = self.intersect(self.hails[i], self.hails[j])
                    if intersection == None:
                        continue
                    x, y, z = intersection
                    if x >= bounding_box[0] and x <= bounding_box[1] and y >= bounding_box[0] and y <= bounding_box[1]:
                        intersections_inside.append(intersection)
            output = len(intersections_inside)
        else:
            line = self.find_intersecting_line(self.hails)
            output = line[0][0] + line[0][1] + line[0][2]
        print(f'Part {'2' if part_2 else '1'}: {output} - {time.time() - start_time}')


def main() -> None:
    day = Day24()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
