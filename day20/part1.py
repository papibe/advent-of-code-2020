import re
import itertools

def getCorners(filename):

    def parseTiles(filename):
        with open(filename, 'r') as fp:
            rawData = fp.read()

        tileLine = re.compile('^Tile (\d+):$')
        rawTiles = rawData.split('\n\n')
        Tiles = {}

        for rawTile in rawTiles:
            if rawTile == "":
                continue

            splitTile = rawTile.splitlines()
            mg = tileLine.match(splitTile[0])
            tileNumber = mg[1]
            tiles = splitTile[1:]

            Tiles[tileNumber] = {
                'ids': {
                    'topStr': ''.join(tiles[0]),
                    'rightStr': ''.join([col[-1] for col in tiles]),
                    'bottomStr': ''.join(tiles[-1]),
                    'leftStr': ''.join([col[0] for col in tiles]),
                },
                'fullTile': tiles
            }
        return Tiles


    def reverseStr(s):
        return s[::-1]


    # main ---------------------------------------------------------------------
    tiles = parseTiles(filename)

    sideIds = {}
    for tileNumber, tile in tiles.items():
        idset = set()
        for _, strValue in tile['ids'].items():
            idset.add(strValue)
            idset.add(reverseStr(strValue))
        sideIds[tileNumber] = idset

    intersections = {tileNumber: set() for tileNumber in tiles}

    combinations = itertools.combinations(list(sideIds.keys()), 2)
    for n, m in combinations:
        inter = sideIds[n] & sideIds[m] # intersection
        intersections[n] = intersections[n] | inter # union
        intersections[m] = intersections[m] | inter # union

    corners = []
    for n, interset in intersections.items():
        if len(interset) == 4:
            corners.append(n)

    return tiles, corners, intersections


def solution(filename):
    tiles, corners, intersections = getCorners(filename)

    product = 1
    for tileNumber in corners:
        product *= int(tileNumber)

    return product


if __name__ == "__main__":
    print(solution("./example.txt"))   # 20899048083289
    print(solution("./input.txt"))
