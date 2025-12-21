from typing import final

@final
class Machine:
    @staticmethod
    def parse(data: str):
        buttons: list[Button] = []
        indicator: Indicator = Indicator([])
        joltage: JoltageCounter = JoltageCounter([])

        for part in data.split(" "):
            part = part.strip()

            if '[' == part[0]:
                indicator = Indicator.parse(part[1:-1])
            elif '(' == part[0]:
                buttons.append(Button(part[1:-1]))
            elif '{' == part[0]:
                joltage = joltage.parse(part[1:-1])

        return Machine(indicator, buttons, joltage)

    def __init__(self, indicator: Indicator, buttons: list[Button], joltage: JoltageCounter):
        self.indicator = indicator
        self.buttons = buttons
        self.joltage = joltage

    def __str__(self) -> str:
        return f"Machine({self.indicator}, {self.buttons}, {self.joltage})"

    def __repr__(self) -> str:
        return str(self)


@final
class Indicator:

    @staticmethod
    def parse(data: str):
        value = [False for _ in range(len(data))]
        for i, c in enumerate(data):
            value[i] = c == '#'
        return Indicator(value)

    def __init__(self, value: list[bool]):
        self.value = value

    def apply(self, button: Button):
        for idx in button.toggleIdx:
            self.value[idx] = not self.value[idx]

    def are_all_off(self) -> bool:
        return not any(self.value)

    def copy(self) -> Indicator:
        return Indicator(self.value.copy())

    def __str__(self) -> str:
        lights = "".join(map(lambda x: '#' if x else '.', self.value))
        return f'Indicator({lights})'

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        return self.value == other.value

class JoltageCounter:
    @staticmethod
    def parse(data: str):
        value = [int(element) for element in data.split(',')]
        return JoltageCounter(value)

    def __init__(self, value: list[int]):
        self.value = value.copy()

    def copy(self):
        return JoltageCounter(self.value.copy())

    def apply_inv(self, button: Button):
        for idx in button.toggleIdx:
            self.value[idx] -= 1

    def is_zero(self):
        return 0 == sum(self.value)

    def __str__(self) -> str:
        return f'JoltageCounter({self.value})'

    def __repr__(self) -> str:
        return str(self)

class Button:
    def __init__(self, data: str):
        self.toggleIdx = [int(element) for element in data.split(',')]

    def __str__(self) -> str:
        return f"Button({self.toggleIdx})"

    def __repr__(self) -> str:
        return str(self)

def solve_part1(machines: list[Machine]) -> int:
    for i, machine in enumerate(machines):
        print(f'machine {i}: {machine}')

    result = 0
    for machine in machines:
        result += find_min_presses_for_indicators(machine)

    return result


def find_min_presses_for_indicators(machine: Machine) -> int:
    queue = [(0, machine.indicator.copy())]
    foundIndicators: list[Indicator] = []
    while len(queue) > 0:
        count, indicator = queue.pop(0)
        print(f'count: {count}, indicator: {indicator}')
        for button in machine.buttons:
            nextIndicator = indicator.copy()
            nextIndicator.apply(button)
            nextCount = count + 1
            print(f'next - count: {nextCount}, indicator: {nextIndicator}')

            if nextIndicator not in foundIndicators:
                foundIndicators.append(nextIndicator)
                if nextIndicator.are_all_off():
                    return nextCount
                else:
                    queue.append((nextCount, nextIndicator))

    return -1

def find_min_presses_for_joltage(machine: Machine) -> int:
    return 0


def solve_part2(machines: list[Machine]) -> int:
    result = 0
    for machine in machines:
        result += find_min_presses_for_joltage(machine)

    return result


def run(part: int = 2, filePath: str = './example.txt'):
    machines = [Machine.parse(line) for line in open(filePath).readlines()]
    for i, machine in enumerate(machines):
        print(f'machine {i}: {machine}')
    print("========")

    if 1 == part:
        result = solve_part1(machines)
    elif 2 == part:
        result = solve_part2(machines)
    else:
        return

    print(f'Result: {result}')


if __name__ == '__main__':
    run()
