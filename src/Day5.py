from utilities.get_input import *
from utilities.parse import *
import time


class Day5:
    def __init__(self) -> None:
        self.input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""" #get_input(2023, 5)
        self.parsed_input = parse_string(self.input)
        seeds, seeds_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = self.parsed_input.split('\n\n')
        self.seeds = [int(seed) for seed in seeds.split(" ")[1:]]
        self.maps = [
            self.parse_map(seeds_to_soil),
            self.parse_map(soil_to_fertilizer),
            self.parse_map(fertilizer_to_water),
            self.parse_map(water_to_light),
            self.parse_map(light_to_temperature),
            self.parse_map(temperature_to_humidity),
            self.parse_map(humidity_to_location.strip('\n'))
        ]
        return
    
    def parse_map(self, input: str) -> list(tuple[int, int, int]):
        map: list(tuple[int, int, int]) = []
        for entry in input.split('\n')[1:]:
            destination, source, range_length = [int(number) for number in entry.split(' ')]
            map.append((destination, source, range_length))
        return map
    


    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        min_location: int = 0
        if not part_2:
            locations = self.seeds.copy()
            for map in self.maps:
                for i, location in enumerate(locations):
                    for destination, source, range_length in map:
                        if location >= source and location < source + range_length:
                            locations[i] = destination + (location - source)
            min_location = min(locations)
        else:
            locations: list(tuple[int,int]) = [(self.seeds[i], self.seeds[i+1]) for i in range(0, len(self.seeds), 2)]
            for map in self.maps:
                new_locations:list(tuple[int,int]) = []
                for i, location_and_length in enumerate(locations):
                    location, length = location_and_length
                    location_end = location + length - 1
                    for destination, source, range_length in map:
                        source_end = source + range_length - 1
                        source_max = max(location, source)
                        source_end_min = min(location_end, source_end)
                        if source_max > source_end_min:
                            continue
                        new_destination = destination + (source_max - source)
                        new_length = source_end_min - source_max + 1
                        new_locations.append((new_destination, new_length))
        print(f'Part {'2' if part_2 else '1'}: {min_location} - {time.time() - start_time}')


def main() -> None:
    day = Day5()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
