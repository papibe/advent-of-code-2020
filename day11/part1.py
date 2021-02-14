def solution(filename):

    EMPTY = 'L'
    OCCUP = '#'
    FLOOR = '.'

    def getNeighborsCoords(i, j):
        return [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),

            (i, j - 1),
            (i, j + 1),

            (i + 1, j + 1),
            (i + 1, j),
            (i + 1, j - 1),
        ]


    def countNeighbors(i, j):
        count = 0
        for row, col in getNeighborsCoords(i, j):
            if row in range(height) and col in range(width):
                if data[row][col] == OCCUP:
                    count += 1

        return count


    # main ---------------------------------------------------------------------

    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    height = len(data)
    width = len(data[0])

    newdata = [[FLOOR for seat in row] for row in data]

    while True:
        change = False

        for i in range(height):
            for j in range(width):
                seat = data[i][j]
                neighbors = countNeighbors(i, j)

                if seat == FLOOR:
                    pass
                elif seat == EMPTY and neighbors == 0:
                    change = True
                    newdata[i][j] = OCCUP
                elif seat == OCCUP and neighbors >= 4:
                    change = True
                    newdata[i][j] = EMPTY
                else:
                    newdata[i][j] = data[i][j]

        if not change:
            break

        data = newdata
        newdata = [[FLOOR for seat in row] for row in data]

    # count occupied seats
    occupiedSeats = 0
    for row in data:
        for seat in row:
            if seat == OCCUP:
                occupiedSeats += 1

    return occupiedSeats


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 37
    print(solution("./input.txt"))
