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
        innerMatrix = self._matrix
        for i in range(self.dimension - 2):
            innerMatrix = innerMatrix[0]

        for i, row in enumerate(initial2DState):
            for j, item in enumerate(row):
                innerMatrix[i][j] = item


    def _insert(self, matrix, space):
        if type(matrix[0]) != np.ndarray:
            # print(type(matrix[0]))
            for i, item in enumerate(space):
                    matrix[i + 1] = item
            return

        for i, subspace in enumerate(space):
            self._insert(matrix[i+1], subspace)


    def insert(self, space):
        self._insert(self._matrix, space._matrix)


    def _getNextItem(self, matrix, pcoord):
        if type(matrix) != np.ndarray:
            yield pcoord, matrix
        else:
            for i, submatrix in enumerate(matrix):
                ncoord = deepcopy(pcoord)
                ncoord.append(i)
                yield from self._getNextItem(submatrix, ncoord)


    def getNextItem(self):
        yield from self._getNextItem(self._matrix, [])


    def countActiveNeighbors(self, oindex, indexes, dim=0):
        if dim == self.dimension:
            if indexes == oindex:
                return 0
            # check boundaries
            for i, coord in enumerate(indexes):
                if coord not in range(self.dims[i]):
                    return 0

            neighbor = self._matrix[tuple(indexes)]
            if neighbor == ACTIVE:
                return 1
            else:
                return 0

        counter = 0
        for distance in (-1, 0, 1):
            nindex = deepcopy(indexes)
            nindex[dim] += distance
            counter += self.countActiveNeighbors(oindex, nindex[:], dim + 1)
        return counter


    def __setitem__(self, index, value):
        self._matrix[tuple(index)] = value


def solution(filename, dimension, cycles=CYCLES):

    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    initialSpace = []
    for line in data:
        row = []
        for item in line:
            row.append(translate[item])
        initialSpace.append(row)

    h = len(initialSpace)
    w = len(initialSpace[0])
    dimensionSizes = [1] * (dimension - 2)  # 2 as in h and w
    dimensionSizes.extend([h, w])

    space = Matrix(*dimensionSizes)
    space.insertData(initialSpace)

    # main cycle
    for cycle in range(cycles):

        tempSpace = Matrix(*[(d+2) for d in space.dims])
        tempSpace.insert(space)
        space = tempSpace
        nextSpace = deepcopy(space)

        for indexes, item in space.getNextItem():
            n = space.countActiveNeighbors(indexes, indexes[:])

            if (item == ACTIVE):
                if (n in [2, 3]):
                    nextSpace[indexes] = ACTIVE
                else:
                    nextSpace[indexes] = INACTIVE
            if (item == INACTIVE):
                if (n == 3):
                    nextSpace[indexes] = ACTIVE
                else:
                    nextSpace[indexes] = INACTIVE

        space = nextSpace

    activeCells = 0
    for indexes, item in space.getNextItem():
        if item == ACTIVE:
            activeCells += 1

    return(activeCells)


if __name__ == "__main__":
    # part 1
    print(solution("./example1.txt", 3, 6)) # 112
    print(solution("./input.txt", 3, 6))
    # part 2
    print(solution("./example1.txt", 4, 6)) # 848
    print(solution("./input.txt", 4, 6))
