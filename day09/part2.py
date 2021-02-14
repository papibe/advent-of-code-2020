import re

def solution(filename, preambleSize):

    def getTarget(preamble, preambleSize, data):
        for number in range(preambleSize, len(data)):
            target = data[number]

            memo = {}
            for n in preamble:
                if n in memo:
                    break
                else:
                    memo[target - n] = n
            else:
                return target

            # update preamble array
            preamble.pop(0)
            preamble.append(target)

        return None # just in case

    # main ---------------------------------------------------------------------

    # read file
    with open(filename, 'r') as fp:
        rawData = fp.read().splitlines()

    data = [int(number) for number in rawData]
    preamble = data[:preambleSize]

    # get number that doesn't have the required property
    target = getTarget(preamble, preambleSize, data)

    # get contiguous set
    start = 0
    end = 1
    setSum = data[start] + data[end]
    while setSum != target:
        if setSum < target:
            end += 1
            setSum += data[end]

        if setSum > target:
            setSum -= data[start]
            start += 1

    contiguousSet = data[start:end]
    return min(contiguousSet) + max(contiguousSet)


if __name__ == "__main__":
    print(solution("./example1.txt", 5))   # 62
    print(solution("./input.txt", 25))
