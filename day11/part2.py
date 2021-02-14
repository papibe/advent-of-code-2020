def solution(filename):

    EMPTY = 'L'
    OCCUP = '#'
    FLOOR = '.'

    def getDirVectors(i, j):
        return [
            (-1, -1),
            (- 1, 0),
            (-1, 1),

            (0, -1),
            (0, 1),

            (1, 1),
            (1, 0),
            (1, -1),
        ]


    def countNeighbors(i, j):
        dirVectors = getDirVectors(i, j)

        count = 0
        for vr, vc in dirVectors:
            nr, nc = (i + vr, j + vc)

            while nr in range(height) and nc in range(width):
                seat = data[nr][nc]
                if data[nr][nc] != FLOOR:
                    if data[nr][nc] == OCCUP:
                        count += 1

                    break
                nr, nc = (nr + vr, nc + vc)

        return count


    # main ---------------------------------------------------------------------

    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    height = len(data)
    width = len(data[0])

    rowRange = range(height)
    colRange = range(width)

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
                elif seat == OCCUP and neighbors >= 5:
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
    print(solution("./example1.txt"))   # 26
    print(solution("./input.txt"))
