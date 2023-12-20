from utilities.get_input import *
from utilities.parse import *
import time
from enum import Enum
from queue import SimpleQueue
import networkx as nx

test_input = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

class Pulse(Enum):
    HIGH = 1
    LOW = 0

class Module:
    def __init__(self, id: str, outputs: str):
        self.id = id
        self.outputs: list[str] = outputs.split(', ')
    
    def connect(self, id: str):
        pass

    def pulse(self, input_id: str, pulse: Pulse) -> list[tuple[str, Pulse]]:
        pass

    def reset(self):
        pass

        
class FlipFlopModule(Module):
    def __init__(self, id: str, outputs: str) -> None:
        super().__init__(id, outputs)
        self.state = False

    def pulse(self, input_id: str, pulse: Pulse) -> list[tuple[str, Pulse]]:
        if pulse == Pulse.LOW:
            self.state = not self.state # Toggle state
            return [(output, Pulse.HIGH if self.state else Pulse.LOW) for output in self.outputs]
        return [] # Do nothing for a high pulse
    
    def reset(self):
        self.state = False

        
class ConjunctionModule(Module):
    def __init__(self, id: str, outputs: str):
        super().__init__(id, outputs)
        self.inputs: dict[str, Pulse] = dict()

    def connect(self, input_id: str):
        self.inputs[input_id] = Pulse.LOW

    def pulse(self, input_id: str, pulse: Pulse) -> list[tuple[str, Pulse]]:
        self.inputs[input_id] = pulse
        if all(pulse == Pulse.HIGH for pulse in self.inputs.values()):
            return [(output, Pulse.LOW) for output in self.outputs]
        return [(output, Pulse.HIGH) for output in self.outputs]
    
    def reset(self):
        for key, _ in self.inputs.items():
            self.inputs[key] = Pulse.LOW

        
class BroadcasterModule(Module):
    def __init__(self, outputs: str):
        super().__init__("broadcaster", outputs)

    def pulse(self, input_id: str, pulse: Pulse) -> list[tuple[str, Pulse]]:
        return [(output, pulse) for output in self.outputs]
    

class ButtonModule(Module):
    def __init__(self):
        super().__init__("button", "broadcaster")

    def pulse(self, input_id: str, pulse: Pulse) -> list[tuple[str, Pulse]]:
        return [(self.outputs[0], Pulse.LOW)]
    
class Day20:
    def __init__(self):
        self.input = get_input(2023, 20)
        self.parsed_input = parse_lines(self.input)
        self.modules = self.parse_modules()

    
    def parse_modules(self) -> dict[str, Module]:
        modules: dict[str, Module] = dict()
        modules["button"] = ButtonModule()
        for line in self.parsed_input:
            id, outputs = line.split(' -> ')
            if id == 'broadcaster':
                modules[id] = BroadcasterModule(outputs)
            elif id[0] == '%':
                modules[id[1:]] = FlipFlopModule(id[1:], outputs)
            elif id[0] == '&':
                modules[id[1:]] = ConjunctionModule(id[1:], outputs)
        # Conjunction need to keep track of their inputs
        for key, value in modules.items():
            for output in value.outputs:
                if modules.get(output) is not None:
                    modules[output].connect(key)
        return modules
    
    def push_button(self) -> tuple[int, int]:
        number_of_high = 0
        number_of_low = 0
        modules_to_pulse = SimpleQueue()
        modules_to_pulse.put(("start", Pulse.LOW, "button"))
        while not modules_to_pulse.empty():
            previous_id, pulse, id = modules_to_pulse.get()
            if self.modules.get(id) is not None:
                for next_id, next_pulse in self.modules[id].pulse(previous_id, pulse):
                    if next_pulse == Pulse.HIGH:
                        number_of_high += 1
                    else:
                        number_of_low += 1
                    modules_to_pulse.put((id, next_pulse, next_id))
        return (number_of_high, number_of_low)

    def solve(self, part_2: bool):
        start_time = time.time()
        output = 0
        if not part_2:
            number_of_high = 0
            number_of_low = 0
            for _ in range(1000):
                number_of_pulses = self.push_button()
                number_of_high += number_of_pulses[0]
                number_of_low += number_of_pulses[1]
            output = number_of_high * number_of_low
        else:
            graph = nx.Graph()
            for key, value in self.modules.items():
                if isinstance(value, ButtonModule):
                    graph.add_node(key, shape='box')
                elif isinstance(value, BroadcasterModule):
                    graph.add_node(key, shape='box')
                elif isinstance(value, FlipFlopModule):
                    graph.add_node(key, shape='circle')
                elif isinstance(value, ConjunctionModule):
                    graph.add_node(key, shape='diamond')
            for key, value in self.modules.items():
                for output in value.outputs:
                    graph.add_edge(key, output)
            os.makedirs("output", exist_ok=True)
            nx.nx_pydot.write_dot(graph, "output/Day20.dot")
        print(f'Part {'2' if part_2 else '1'}: {output} - {time.time() - start_time}')


def main():
    day = Day20()
    day.solve(False)
    day.solve(True)


if __name__ == "__main__":
    main()
