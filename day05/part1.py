from math import floor, ceil

def solution(filename):

    def decode(bordingPass, lower, upper):
        for char in bordingPass:
            if char == 'B' or char == 'R':
                lower = ceil((upper + lower)/2)
            if char == 'F' or char == 'L':
                upper = floor((upper + lower)/2)
        return lower


    # main ---------------------------------------------------------------------

    # read file
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    maxId = -1
    # decode 2 parts of the boarding passes
    for bordingPass in data:
        row = decode(bordingPass[:-3], lower=0, upper=127)
        column = decode(bordingPass[-3:], lower=0, upper=7)

        seatId = row * 8 + column

        if seatId > maxId:
            maxId = seatId

    return maxId


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 357
    print(solution("./inputs/example2.txt"))   # 567
    print(solution("./inputs/example3.txt"))   # 119
    print(solution("./inputs/example4.txt"))   # 820
    print(solution("./inputs/input.txt"))
