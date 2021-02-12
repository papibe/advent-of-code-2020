def solution(filename):
    TREE = '#'

    # read file
    with open(filename, 'r') as fp:
        worldMap = fp.read().splitlines()

    # dimensions
    width = len(worldMap[0])
    height = len(worldMap)

    rowSlope = 1
    colSlope = 3
    row = col = 0

    trees = 0
    while row < height:
        if worldMap[row][col] == TREE:
            trees += 1

        row += rowSlope
        col = (col + colSlope) % (width)

    return trees


if __name__ == "__main__":
    print(solution("./example1.txt"))
    print(solution("./index.txt"))
