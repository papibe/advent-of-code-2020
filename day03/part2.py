def solution(filename):
    TREE = '#'

    def tobogganTravel(worldMap, colSlope, rowSlope):
        # dimensions
        width = len(worldMap[0])
        height = len(worldMap)

        trees = 0
        row = col = 0   # initial position
        while row < height:
            if worldMap[row][col] == TREE:
                trees += 1

            row += rowSlope
            col = (col + colSlope) % (width)

        return trees


    # read file
    with open(filename, 'r') as fp:
        worldMap = fp.read().splitlines()

    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    answer = 1  # multiplication of encountered trees
    
    for colSlope, rowSlope in slopes:
        answer = answer * tobogganTravel(worldMap, colSlope, rowSlope)

    return answer


if __name__ == "__main__":
    print(solution("./example1.txt"))
    print(solution("./index.txt"))
