from aocd import numbers, submit

# https://adventofcode.com/2021/day/1

def part1():
    count = 0
    prev = None
    for i in numbers:
        if prev:
            if i > prev :
                count+=1
        prev = i

    return count


def part2():
    window_size = 3
    count = 0
    prev = None
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        if prev:
            if sum(window) > prev:
                count+=1
        prev = sum(window)
    
    return count


if __name__ == "__main__":
    submit(part1())
    submit(part2())