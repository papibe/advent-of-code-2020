def solution(filename):
    INITIAL = 1
    DIVN = 20201227
    SUBJECT = 7

    def getKeys(filename):
        with open(filename, 'r') as fp:
            data = fp.read().splitlines()
        return int(data[0]), int(data[1])


    def getLoopSize(n):
        loopSize = 0
        value = INITIAL
        while value != n:
            value = (value * SUBJECT) % DIVN
            loopSize += 1
        return loopSize


    def transform(subject, loopSize):
        value = INITIAL
        for _ in range(loopSize):
            value = (value * subject) % DIVN
        return value


    # main ---------------------------------------------------------------------
    cardPK, doorPK  = getKeys(filename)

    cardLS = getLoopSize(cardPK)
    doorLS = getLoopSize(doorPK)

    ek_1 = transform(cardPK, doorLS)
    ek_2 = transform(doorPK, cardLS)

    if ek_1 != ek_2:
        return None

    return ek_1

if __name__ == "__main__":

    print(solution("./example.txt"))   # 14897079
    print(solution("./input.txt"))
