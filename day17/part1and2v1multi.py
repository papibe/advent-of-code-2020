from copy import deepcopy

ACTIVE = '#'
INACTIVE = '.'
CYCLES = 6


class Matrix():

    def __init__(self, *dims):
        self.dims = list(dims)
        self.dimension = len(dims)
        self._shortcuts = [i for i in self._create_shortcuts(dims)]
        self._array = [INACTIVE] * (self._shortcuts.pop())
        self._shortcuts.reverse()


    def _create_shortcuts(self, dims):
        dimList = list(dims)
        dimList.reverse()
        number = 1
        yield 1
        for i in dimList:
            number *= i
            yield number


    def _flat_index(self, index):
        if len(index) != len(self._shortcuts):
            raise TypeError()

        flatIndex = 0
        for i, num in enumerate(index):
            flatIndex += num * self._shortcuts[i]
        return flatIndex


    def __getitem__(self, index):
        return self._array[self._flat_index(index)]


    def __setitem__(self, index, value):
        self._array[self._flat_index(index)] = value


    def get_dim_indexes(self, flatIndex):
        indexes = []
        for i, num in enumerate(self._shortcuts):
            div = flatIndex // self._shortcuts[i]
            rem = flatIndex % self._shortcuts[i]
            indexes.append(div)
            flatIndex = rem
        return indexes


    def insertData(self, initialState):
        index = [0] * (self.dimension - 2)
        for h, row in enumerate(initialState):
            for w, item in enumerate(row):
                self._array[self._flat_index(index + [h, w])] = item


    def countActiveNeighbors(self, oindex, indexes, dim=0):
        if dim == self.dimension:
            if indexes == oindex:
                return 0
            for i, coord in enumerate(indexes):
                if coord not in range(self.dims[i]):
                    return 0

            neighbor = self._array[self._flat_index(indexes)]
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


    def insert(self, matrix):
        for flatIndex, item in enumerate(matrix._array):
            indexes = matrix.get_dim_indexes(flatIndex)
            for i in range(len(indexes)):
                indexes[i] += 1
            self._array[self._flat_index(indexes)] = item


    def totalActives(self):
        counter = 0
        for item in self._array:
            if item == ACTIVE:
                counter += 1
        return counter


def solution(filename, dimension, cycles=CYCLES):

    # main ---------------------------------------------------------------------
    with open(filename, 'r') as fp:
        data = fp.read().splitlines()

    initialSpace = [list(row) for row in data]
    h = len(initialSpace)
    w = len(initialSpace[0])
    dimensionSizes = [1] * (dimension - 2)  # 2 as in h and w
    dimensionSizes.extend([h, w])

    space = Matrix(*dimensionSizes)

    space.insertData(initialSpace)

    for cycle in range(cycles):

        tempSpace = Matrix(*[(d+2) for d in space.dims])
        tempSpace.insert(space)
        space = tempSpace
        nextSpace = deepcopy(space)

        for flatIndex, item in enumerate(space._array):
            indexes = space.get_dim_indexes(flatIndex)
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

    return space.totalActives()


if __name__ == "__main__":
    # part 1
    print(solution("./example1.txt", 3, 6)) # 112
    print(solution("./input.txt", 3, 6))
    # part 2
    print(solution("./example1.txt", 4, 6)) # 848
    print(solution("./input.txt", 4, 6))
