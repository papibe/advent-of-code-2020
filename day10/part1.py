import re

def solution(filename):
    # read file
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    adapters = [int(number) for number in data]
    adapters.sort()
    adapters.append(adapters[-1] + 3) # add representation of device

    differences = [0, 0, 0, 0]
    charger = 0

    for adapter in adapters:
        diff = adapter - charger

        if diff <= 3:
            charger = adapter
            differences[diff] += 1

    return differences[1] * differences[3]


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 35 = 7 * 5
    print(solution("./inputs/example2.txt"))   # 220 = 22 * 10
    print(solution("./inputs/input.txt"))
