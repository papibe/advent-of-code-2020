import re

def solution(filename):

    def simpleMove(action, units, curEpos, curNpos):
        if action == 'N':
            curNpos += units

        if action == 'S':
            curNpos -= units

        if action == 'E':
            curEpos += units

        if action == 'W':
            curEpos -= units

        return (curEpos, curNpos)


    def matrixMult(vector, matrix):
        result = [
            vector[0]*matrix[0][0] + vector[1]*matrix[1][0],
            vector[0]*matrix[0][1] + vector[1]*matrix[1][1]
        ]
        return result


    def rotate(dir, angle, x, y):
        LrotMatix = {
            90: [[0, 1], [-1, 0]],
            180: [[-1, 0], [0, -1]],
            270: [[0, -1], [1, 0]],
        }
        RrotMatix = {
            90: [[0, -1], [1, 0]],
            180: [[-1, 0], [0, -1]],
            270: [[0, 1], [-1, 0]],
        }

        if dir == 'L':
            matrix = LrotMatix[angle]
        if dir == 'R':
            matrix = RrotMatix[angle]

        return matrixMult([x, y], matrix)


    # main ---------------------------------------------------------------------
    with open(filename, 'r') as fp:
        navigationInstructions = fp.read().splitlines()

    directionRE = re.compile('(\w)(\d+)')

    currentE = 0
    currentN = 0
    facing = 'E'

    wayPE = 10
    wayPN = 1

    for instruction in navigationInstructions:
        mg = directionRE.match(instruction)
        action = mg[1]
        units = int(mg[2])

        if action in ['N', 'S', 'E', 'W']:
            wayPE, wayPN = simpleMove(action, units, wayPE, wayPN)

        if action in ['L', 'R']:
            wayPE, wayPN = rotate(action, units, wayPE, wayPN)

        if action == 'F':
            currentE += wayPE * units
            currentN += wayPN * units

    return abs(currentE) + abs(currentN)

if __name__ == "__main__":
    print(solution("./example1.txt"))   # 286
    print(solution("./input.txt"))
