import re
from copy import copy, deepcopy

def solution(filename):

    ACTIVE = '#'
    INACTIVE = '.'
    CYCLES = 6

    def emptySpace(space):
        return deepcopy(space)


    def totalActives(space):
        actives = 0
        for z, plane in enumerate(space):
            for y, row in enumerate(plane):
                for x, element in enumerate(row):
                    if element == ACTIVE:
                        actives += 1
        return actives


    def addZplanes(space, zsize, ysize, xsize):
        zplane1 = [['.']*xsize for i in range(ysize)]
        space.insert(0, zplane1)
        zplane2 = [['.']*xsize for i in range(ysize)]
        space.append(zplane2)


    def addYplanes(space, zsize, ysize, xsize):
        for z, plane in enumerate(space):
            xplane1 = ['.']*xsize
            plane.insert(0, xplane1)
            xplane2 = ['.']*xsize
            plane.append(xplane2)


    def addXplanes(space, zsize, ysize, xsize):
        for z, plane in enumerate(space):
            for y, row in enumerate(plane):
                row.insert(0, '.')
                row.append('.')


    def add6Planes(space):
        zsize = len(space)
        ysize = len(space[0])
        xsize = len(space[0][0])

        addZplanes(space, zsize, ysize, xsize)
        addYplanes(space, zsize, ysize, xsize)
        addXplanes(space, zsize, ysize, xsize)


    def countActiveNeighbors(space, z, y, x, element):
        zsize = len(space)
        ysize = len(space[0])
        xsize = len(space[0][0])

        counter = 0
        activeNeighbors = 0
        distance = (1, 0, -1)
        for zstep in distance:
            for ystep in distance:
                for xstep in distance:
                    nz = z + zstep
                    ny = y + ystep
                    nx = x + xstep
                    if (nz == z) and (ny == y) and (nx == x):
                        continue
                    if  (nz not in range(zsize)) or \
                        (ny not in range(ysize)) or \
                        (nx not in range(xsize)):
                        continue
                    if space[nz][ny][nx] == ACTIVE:
                        activeNeighbors += 1
                    counter += 1
        return activeNeighbors


    # main ---------------------------------------------------------------------
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    splitData = []
    for row in data:
        splitData.append(list(row))
    space = [splitData]

    for cycle in range(CYCLES):
        # add empty planes around current space
        add6Planes(space)
        nextSpace = emptySpace(space)

        for z, plane in enumerate(space):
            for y, row in enumerate(plane):
                for x, element in enumerate(row):
                    n = countActiveNeighbors(space, z, y, x, element)
                    if (element == ACTIVE):
                        if (n in [2, 3]):
                            nextSpace[z][y][x] = ACTIVE
                        else:
                            nextSpace[z][y][x] = INACTIVE
                    if (element == INACTIVE):
                        if (n == 3):
                            nextSpace[z][y][x] = ACTIVE
                        else:
                            nextSpace[z][y][x] = INACTIVE

        space = nextSpace

    return totalActives(space)


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 112
    print(solution("./input.txt"))
