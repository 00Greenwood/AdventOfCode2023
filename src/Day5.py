from utilities.get_input import *
from utilities.parse import *
import time


class Day5:
    def __init__(self) -> None:
        self.input = get_input(2023, 5)
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
                new_locations: list(tuple[int,int]) = []
                for location_and_length in locations:
                    location, length = location_and_length
                    location_end = location + length - 1
                    locations_to_add = []
                    for destination, source, range_length in map:
                        source_end = source + range_length - 1
                        source_max = max(location, source)
                        source_end_min = min(location_end, source_end)
                        # Missing everything
                        if source_max > source_end_min:
                            continue
                        new_destination = destination + (source_max - source)
                        new_length = source_end_min - source_max + 1
                        locations_to_add.append((new_destination, new_length))
                        # Missing start
                        if location < source_max:
                            locations.append((location, length - new_length))
                        # Missing end
                        if location_end > source_end_min:
                            locations.append((source_end_min + 1, length - new_length))
                        # Mapping found
                        break
                    # No mappings found
                    if len(locations_to_add) == 0:
                        locations_to_add.append((location, length))
                    new_locations += locations_to_add
                locations = new_locations
            min_location = min([location for location, length in locations])
        print(f'Part {'2' if part_2 else '1'}: {min_location} - {time.time() - start_time}')


def main() -> None:
    day = Day5()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
