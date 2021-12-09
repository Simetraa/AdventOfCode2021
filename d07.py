from aocd import data, submit

# https://adventofcode.com/2021/day/7

crabs = [int(x) for x in data.split(",")]

def part1():
    costs = []
    for move_to in crabs:
        fuel_cost = 0
        for move_from in crabs:
            difference = abs(move_to - move_from)
            fuel_cost += difference
        costs.append(fuel_cost)

    return min(costs)


def calculate_fuel_cost(move_to, move_from):
    difference = abs(move_to - move_from)
    fuel_cost = difference * (difference + 1) / 2
    return fuel_cost


def part2():
    costs = []
    for move_to in crabs:
        fuel_cost = 0
        for move_from in crabs:
            fuel_cost += calculate_fuel_cost(move_to, move_from)
        costs.append(fuel_cost)

    return round(min(costs))


if __name__ == "__main__":
    submit(part1())
    submit(part2())
