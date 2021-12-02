from aocd import lines, submit

# https://adventofcode.com/2021/day/2

def part1():
    x, depth = 0, 0
    for line in lines:
        instruction, value = line.split()
        value = int(value)
        if instruction == "forward":
            x += value
        elif instruction == "up":
            depth -= value
        elif instruction == "down":
            depth += value
    return x * depth

def part2():
    x, depth, aim = 0, 0, 0
    for line in lines:
        instruction, value = line.split()
        value = int(value)
        if instruction == "forward":
            x += value
            depth += aim * value
        elif instruction == "up":
            aim -= value
        elif instruction == "down":
            aim += value
    return x * depth


if __name__ == "__main__":
    submit(part1())
    submit(part2())
