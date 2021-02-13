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

    seatIdsMap = {}

    maxId = -1
    # decode 2 parts of the boarding passes
    for bordingPass in data:
        row = decode(bordingPass[:-3], lower=0, upper=127)
        column = decode(bordingPass[-3:], lower=0, upper=7)

        seatIdsMap[row * 8 + column] = True

    # search for my seat
    for seatId in range(len(data)+1):
        if seatId not in seatIdsMap:
            if (seatId+1) in seatIdsMap and (seatId-1) in seatIdsMap:
                return seatId


if __name__ == "__main__":
    print(solution("./inputs/input.txt"))
