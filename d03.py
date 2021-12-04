from typing import Counter
from aocd import lines, submit
from statistics import mode

# https://adventofcode.com/2021/day/3

def part1():
    gamma = []
    epsilon = []
    rotated = list(zip(*lines[::-1]))
    for col in rotated:
        gamma.append(mode(col))

    for col in rotated:
        epsilon.append('1' if mode(col) == '0' else '0')
    
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)


    return int(gamma, 2) * int(epsilon, 2)

def part2():
    LENGTH = len(lines[0])
    gamma = lines[:]
    epsilon = lines[:]

    for bit in range(LENGTH):
        mode = Counter([line[bit] for line in gamma])
        mode = '1' if mode['1'] >= mode['0'] else '0'
        gamma = list(filter(lambda x: x[bit] == mode, gamma))
        gamma = [line for line in gamma if line[bit] == mode]
        if len(gamma) == 1:
            break

    for bit in range(LENGTH):
        mode = Counter([line[bit] for line in epsilon])
        inverted_mode = '0' if mode['1'] >= mode['0'] else '1'
        epsilon = [line for line in epsilon if line[bit] == inverted_mode]
        if len(epsilon) == 1:
            break

    return int(epsilon[0], 2) * int(gamma[0], 2)


if __name__ == "__main__":
    submit(part1())
    submit(part2())
