import re
import itertools
import math
from copy import copy, deepcopy
from part1 import getCorners

def rot90(tiles, tilen):
    tile = tiles[tilen]
    n = len(tile)  # matix size
    rot = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rot[i][j] = tile[n - j - 1][i]
    tiles[tilen] = rot

def hflip(tiles, tilen):
    tile = tiles[tilen]
    n = len(tile)  # matix size
    flip = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            flip[i][j] = tile[n - i - 1][j]
    tiles[tilen] = flip


def transformation(tiles, n, orientation):
    standard = ["0", "90", "180", "270"]
    if orientation in standard:
        for _ in range(standard.index(orientation)):
            rot90(tiles, n)
        return

    if orientation == "hflip":
        hflip(tiles, n)
        return

    standardF = ["_", "90f", "180f", "270f"]
    if orientation in standardF:
        hflip(tiles, n)
        for _ in range(standardF.index(orientation)):
            rot90(tiles, n)
        return


def reverseStr(s):
    return s[::-1]


class RotTile():
    def __init__(self, rotation, tileStr):
        self.rotation = rotation
        self.tileStr = tileStr


class Tile():
    def __init__(self, tileStr):
        self.rotTiles = {}
        self.rawTile = tileStr
        self.rotTiles["0"] = tileStr
        self.position = None

    def addRotation(self, tileNumber, angle):
        if angle in ["0", "90", "180", "270", "hflip"]:
            self.rotTiles[angle] = self.rotateTile(tileNumber, angle, self.rawTile)

        elif angle in ["90f", "180f", "270f"]:
            self.rotTiles[angle] = self.rotateTile(tileNumber, angle, self.rotTiles['hflip'])


    def rotateTile(self, tileNumber, angle, tile):
        if angle == "0":
            rotTile = tile

        if angle in ["90", "90f"]:
            rotTile = {
                'topStr': reverseStr(tile['leftStr']),
                'rightStr': tile['topStr'],
                'bottomStr': reverseStr(tile['rightStr']),
                'leftStr': tile['bottomStr'],
            }
        if angle in ["180", "180f"]:
            rotTile = {
                'topStr': reverseStr(tile['bottomStr']),
                'rightStr': reverseStr(tile['leftStr']),
                'bottomStr': reverseStr(tile['topStr']),
                'leftStr': reverseStr(tile['rightStr']),
            }
        if angle in ["270", "270f"]:
            rotTile = {
                'topStr': tile['rightStr'],
                'rightStr': reverseStr(tile['bottomStr']),
                'bottomStr': tile['leftStr'],
                'leftStr': reverseStr(tile['topStr']),
            }
        if angle == "hflip":
            rotTile = {
                'topStr': tile['bottomStr'],
                'rightStr': reverseStr(tile['rightStr']),
                'bottomStr': tile['topStr'],
                'leftStr': reverseStr(tile['leftStr']),
            }
        return rotTile


def solution(filename):

    # main ---------------------------------------------------------------------
    rawTiles, corners, intersections = getCorners(filename)

    tiles = {}
    for tileNumber, rawTile in rawTiles.items():
        tiles[tileNumber] = Tile(rawTile['ids'])

    for tileNumber, tile in tiles.items():
        for angle in ["0", "90", "180", "270", "hflip", "90f", "180f", "270f"]:
            tile.addRotation(tileNumber, angle)

    # get which transformation can be use for the upper left corner
    cornerTileN = corners[0]
    corner = tiles[cornerTileN]
    for position in ["0", "90", "180", "270", "hflip", "90f", "180f", "270f"]:
        if (corner.rotTiles[position]['topStr'] not in intersections[cornerTileN]) \
            and (corner.rotTiles[position]['leftStr'] not in intersections[cornerTileN]):
            properangle = position
            break

    corner.position = properangle
    gridSize = int(math.sqrt(len(tiles)))
    grid = [[None]*gridSize for _ in range(gridSize)]

    matchingTiles = deepcopy(tiles)
    del matchingTiles[cornerTileN]

    # first row
    grid[0][0] = cornerTileN
    for i in range(1, gridSize):
        previousTileId = grid[0][i - 1]
        previousTile = tiles[previousTileId]
        orientation = previousTile.position
        idToMach = previousTile.rotTiles[orientation]['rightStr']

        for tileNumber, tile in matchingTiles.items():
            for position in ["0", "90", "180", "270", "hflip", "90f", "180f", "270f"]:
                if tile.rotTiles[position]['leftStr'] == idToMach:
                    tiles[tileNumber].position = position
                    nextTileId = tileNumber
                    break

        del matchingTiles[nextTileId]
        grid[0][i] = nextTileId

    # rest of the grid
    for row in range(1, gridSize):
        for col in range(gridSize):
            upperTileId = grid[row - 1][col]
            upperTile = tiles[upperTileId]
            orientation = upperTile.position
            idToMach = upperTile.rotTiles[orientation]['bottomStr']

            for tileNumber, tile in matchingTiles.items():
                for position in ["0", "90", "180", "270", "hflip", "90f", "180f", "270f"]:
                    if tile.rotTiles[position]['topStr'] == idToMach:
                        tiles[tileNumber].position = position
                        nextTileId = tileNumber
                        break

            del matchingTiles[nextTileId]
            grid[row][col] = nextTileId

    # remove borders
    SlimTiles = {}
    for n, tile in rawTiles.items():
        newtile = []
        for i in range(1, len(tile['fullTile']) - 1):
            newtile.append(tile['fullTile'][i][:-1][1:])
        SlimTiles[n] = newtile

    for row in grid:
        for tileN in row:
            orientation = tiles[tileN].position
            transformation(SlimTiles, tileN, orientation)

    tilesize = len(SlimTiles[grid[0][0]])
    imageSize = gridSize * tilesize
    finalImage = [[None]*imageSize for _ in range(imageSize)]

    # create final image
    for rown, row in enumerate(grid):
        imageRow = []
        for coln, tileN in enumerate(row):
            tile = SlimTiles[tileN]
            for i, tilerow in enumerate(tile):
                for j, item in enumerate(tilerow):
                    imagI = rown*tilesize + i
                    imagJ = coln*tilesize + j
                    finalImage[imagI][imagJ] = tile[i][j]

    dragon = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    dragonCoords = []
    for i, row in enumerate(dragon):
        for j, item in enumerate(row):
            if item == "#":
                dragonCoords.append((i,j))

    FinalImageD = {
        0: finalImage
    }

    # look for dragons in all possible transformations
    for trans in ["0", "90", "180", "270", "hflip", "90f", "180f", "270f"]:
        transformation(FinalImageD, 0, trans)
        finalImageO = FinalImageD[0]
        finalImage = deepcopy(finalImageO)
        findDragon = False
        for i, row in enumerate(finalImage):
            for j, item in enumerate(row):
                matches = 0
                dcoords = []
                for di, dj in dragonCoords:
                    checki = i + di
                    checkj = j + dj
                    if checki < imageSize and checkj < imageSize:
                        if finalImage[checki][checkj] == "#":
                            matches += 1
                            dcoords.append((checki, checkj))
                        else:
                            break
                    else:
                        break

                if matches == len(dragonCoords):
                    findDragon = True
                    for di, dj in dcoords:
                        finalImage[di][dj] = "O"

        if findDragon:
            break

    return len([1 for row in finalImage for item in row if item == '#'])


if __name__ == "__main__":
    print(solution("./example.txt"))   # 273
    print(solution("./input.txt"))
