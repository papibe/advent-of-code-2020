import numpy as np
from copy import deepcopy

INACTIVE = 0
ACTIVE = 1
CYCLES = 6

translate = {
    '.': INACTIVE,
    '#': ACTIVE
}

class Matrix():

    def __init__(self, *dims):
        self.dims = list(dims)
        self.dimension = len(dims)

        # number of nodes
        size = 1
        for dim in dims:
            size *= dim

        self._matrix = np.zeros((size,), dtype=int).reshape(*self.dims)


    def insertData(self, initial2DState):
        for y, row in enumerate(initial2DState):
            for x, element in enumerate(row):
                self._matrix[0, 0, y, x] = translate[element]


    def _insert(self, matrix, space):
        for w, cube in enumerate(space):
            for z, plane in enumerate(cube):
                for y, row in enumerate(plane):
                    for x, element in enumerate(row):
                        matrix[w + 1, z + 1, y + 1, x + 1] = element


    def insert(self, space):
        self._insert(self._matrix, space._matrix)


    def countActiveNeighbors(self, w, z, y, x):
        wsize = len(self._matrix)
        zsize = len(self._matrix[0])
        ysize = len(self._matrix[0][0])
        xsize = len(self._matrix[0][0][0])

        activeNeighbors = 0
        distance = (1, 0, -1)
        for wstep in distance:
            for zstep in distance:
                for ystep in distance:
                    for xstep in distance:
                        nw = w + wstep
                        nz = z + zstep
                        ny = y + ystep
                        nx = x + xstep

                        if (nw == w) and (nz == z) and (ny == y) and (nx == x):
                            continue
                        if  (nw not in range(wsize)) or \
                            (nz not in range(zsize)) or \
                            (ny not in range(ysize)) or \
                            (nx not in range(xsize)):
                            continue
                        if self._matrix[nw][nz][ny][nx] == ACTIVE:
                            activeNeighbors += 1

        return activeNeighbors


    def __setitem__(self, index, value):
        self._matrix[tuple(index)] = value


    def countActiveCells(self):
        activeCells = 0
        for w, cube in enumerate(self._matrix):
            for z, plane in enumerate(cube):
                for y, row in enumerate(plane):
                    for x, element in enumerate(row):
                        if element == ACTIVE:
                            activeCells += 1
        return activeCells


def solution(filename, cycles=CYCLES):

    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    initialSpace = [list(row) for row in data]
    h = len(initialSpace)
    w = len(initialSpace[0])

    space = Matrix(*[1, 1, h, w])
    space.insertData(initialSpace)

    # main cycle
    for cycle in range(cycles):

        tempSpace = Matrix(*[(d+2) for d in space.dims])
        tempSpace.insert(space)
        space = tempSpace
        nextSpace = deepcopy(space)

        for w, cube in enumerate(space._matrix):
            for z, plane in enumerate(cube):
                for y, row in enumerate(plane):
                    for x, element in enumerate(row):
                        indexes = [w, z, y, x]
                        n = space.countActiveNeighbors(*indexes)

                        if (element == ACTIVE):
                            if (n in [2, 3]):
                                nextSpace[indexes] = ACTIVE
                            else:
                                nextSpace[indexes] = INACTIVE
                        if (element == INACTIVE):
                            if (n == 3):
                                nextSpace[indexes] = ACTIVE
                            else:
                                nextSpace[indexes] = INACTIVE

        space = nextSpace

    return space.countActiveCells()


if __name__ == "__main__":
    print(solution("./example1.txt", 6)) # 848
    print(solution("./input.txt", 6))
