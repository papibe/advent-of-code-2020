def solution(filename):
    step = {
        'se': [-1, 1],
        'e': [0, 2],
        'ne': [1, 1],
        'nw': [1, -1],
        'w': [0, -2],
        'sw': [-1, -1],
    }
    EMPTY = '.'
    BLACK = 'B'
    WHITE = 'W'

    def parseDirections(filename):
        with open(filename, 'r') as fp:
            data = fp.read().splitlines()

        # parse directions
        flippedList = []
        for line in data:
            index = 0
            directions = []
            while index < len(line):
                direction = line[index]
                if (direction == 'e') or (direction == 'w'):
                    directions.append(direction)
                    index += 1
                else:
                    directions.append(line[index:index+2])
                    index += 2
            flippedList.append(directions)
        return flippedList


    def navegate(pos, _dir):
        return [pos[0] + step[_dir][0], pos[1] + step[_dir][1]]


    def fillFloor(floor, tiles):
        for tile, value in tiles.items():
            pos, isBlack = value
            if isBlack:
                newRow = pos[0] + max_rows
                newCol = pos[1] + max_cols
                floor[newRow][newCol] = BLACK


    def nextT(tile):
        if tile == EMPTY:
            return WHITE

        if tile == WHITE:
            return EMPTY


    def widenFloor(floor, start):
        # add another row at begining and end
        newRow = []
        dstart = start
        for _ in range(len(floor[0])+2):
            newRow.append(dstart)
            dstart = nextT(dstart)

        floor.insert(0, newRow)
        floor.append(newRow)

        # add a new column at the start and at the end
        dstart = nextT(start)
        index = 1
        while index < len(floor) - 1:
            row = floor[index]
            row.insert(0, dstart)
            row.append(dstart)
            dstart = nextT(dstart)
            index += 1


    def countBlackNeighbors(row, col, floor):
        neighbors = 0
        for _dir, value in step.items():
            sr, sc = value
            nr = row + sr
            nc = col + sc
            if (nr < len(floor)) and (nc < len(floor[0])):
                if floor[nr][nc] == BLACK:
                    neighbors += 1
        return neighbors


    def countBlackTiles(floor):
        counter = 0
        for row in floor:
            for tile in row:
                if tile == BLACK:
                    counter += 1
        return counter


    # main ---------------------------------------------------------------------
    flippedList = parseDirections(filename)

    tiles = {}
    rows = []
    cols = []

    for directions in flippedList:
        current = [0, 0]
        for direction in directions:
            current = navegate(current, direction)

        rows.append(current[0])
        cols.append(current[1])

        tilekey = f'{current[0]},{current[1]}'

        if tilekey not in tiles:
            tiles[tilekey] = (current, True)
        else:
            tiles[tilekey] = (tiles[tilekey][0],not tiles[tilekey][1])

    # create a matrix to represent the floor
    max_rows = max(rows)
    min_rows = min(rows)
    max_cols = max(cols)
    min_cols = min(cols)
    aBlackTile = [rows[0] + max_rows, cols[0] + max_cols]
    if (aBlackTile[0] % 2) == 1 and (aBlackTile[1] % 2) == 1:
        start = WHITE
    else:
        start = EMPTY

    floor = [[EMPTY] * (max_cols - min_cols + 1) for _ in range(max_rows - min_rows + 1)]
    fillFloor(floor, tiles)
    widenFloor(floor, start)
    newfloor = [[EMPTY] * len(floor[0]) for _ in range(len(floor))]

    dstart = start
    for i, row in enumerate(floor):
        for j, tile in enumerate(row):
            if floor[i][j] == BLACK:
                pass
            else:
                floor[i][j] = dstart
            dstart = nextT(dstart)

    # Applying art rules
    for day in range(1, 100 + 1):
        newfloor = [[EMPTY] * len(floor[0]) for _ in range(len(floor))]
        for i, row in enumerate(floor):
            for j, tile in enumerate(row):
                if tile == EMPTY:
                    continue

                n = countBlackNeighbors(i, j, floor)
                if tile == BLACK:
                    if (n == 0) or (n > 2):
                        newfloor[i][j] = WHITE
                        continue

                if tile == WHITE:
                    if n == 2:
                        newfloor[i][j] = BLACK
                        continue

                newfloor[i][j] = floor[i][j]

        floor = newfloor
        widenFloor(floor, start)

    return countBlackTiles(newfloor)

if __name__ == "__main__":
    print(solution("./example.txt"))    # 2208
    print(solution("./input.txt"))
