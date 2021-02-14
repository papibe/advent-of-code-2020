import re

def solution(filename):

    rightRotation = {
        'E': { 90: 'S', 180: 'W', 270: 'N'},
        'S': { 90: 'W', 180: 'N', 270: 'E'},
        'W': { 90: 'N', 180: 'E', 270: 'S'},
        'N': { 90: 'E', 180: 'S', 270: 'W'},
    }
    leftRotation = {
        'E': { 90: 'N', 180: 'W', 270: 'S'},
        'S': { 90: 'E', 180: 'N', 270: 'W'},
        'W': { 90: 'S', 180: 'E', 270: 'N'},
        'N': { 90: 'W', 180: 'S', 270: 'E'},
    }


    def simpleMove(action, unit, curEpos, curNpos):
        if action == 'N':
            curNpos += units

        if action == 'S':
            curNpos -= units

        if action == 'E':
            curEpos += units

        if action == 'W':
            curEpos -= units

        return (curEpos, curNpos)


    # main ---------------------------------------------------------------------
    with open(filename, 'r') as fp:
        navigationInstructions = fp.read().splitlines()

    directionRE = re.compile('(\w)(\d+)')

    currentE = 0
    currentN = 0
    facing = 'E'

    for instruction in navigationInstructions:
        mg = directionRE.match(instruction)
        action = mg[1]
        units = int(mg[2])

        if action in ['N', 'S', 'E', 'W']:
            currentE, currentN = simpleMove(action, units, currentE, currentN)

        if action == 'L':
            facing = leftRotation[facing][units]

        if action == 'R':
            facing = rightRotation[facing][units]

        if action == 'F':
            currentE, currentN = simpleMove(facing, units, currentE, currentN)

    return abs(currentE) + abs(currentN)


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 25
    print(solution("./input.txt"))
