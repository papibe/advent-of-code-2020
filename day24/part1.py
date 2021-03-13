def solution(filename):
    step = {
        'se': [-1, 1],
        'e': [0, 2],
        'ne': [1, 1],
        'nw': [1, -1],
        'w': [0, -2],
        'sw': [-1, -1],
    }

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


    # main ---------------------------------------------------------------------
    flippedList = parseDirections(filename)

    tiles = {}
    for directions in flippedList:
        current = [0, 0]
        for direction in directions:
            current = navegate(current, direction)

        tilekey = f'{current[0]},{current[1]}'

        if tilekey not in tiles:
            tiles[tilekey] = True
        else:
            tiles[tilekey] = not tiles[tilekey]

    return len([1 for tile, value in tiles.items() if value])

if __name__ == "__main__":
    print(solution("./example.txt"))   # 10
    # print(solution("./input.txt"))
