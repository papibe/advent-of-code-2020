import re

def solution(filename):

    def convertToBitMask(s):
        mask1 = 0
        mask0 = 2**36 - 1   # 36 bits of 1's

        for i, char in enumerate(s):
            index = len(s) - i - 1
            # mask of 1s
            if char == '1':
                mask1 |= (1 << index)

            # mask of zeros
            if char == '0':
                mask0  -= (1 << index)

        return (mask1, mask0)


    # read file
    with open(filename, 'r') as fp:
        initializationProgram = fp.read().splitlines()

    remaskRE = re.compile('^mask = (\w+)$')
    rememRE = re.compile('^mem\[(\d+)\] = (\d+)$')

    memory = {}
    for line in initializationProgram:
        # matching groups
        maskMG = remaskRE.match(line)
        memMG = rememRE.match(line)

        # line is a mask
        if maskMG is not None:
            mask = maskMG[1]
            bitmask1, bitmask0 = convertToBitMask(mask)

        # line is a mem instruction
        if memMG is not None:
            address = int(memMG[1])
            value = int(memMG[2])

            value |= bitmask1
            value &= bitmask0
            memory[address] = value

    # return the sum all values in memory
    return sum(memory.values())


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))   # 165
    print(solution("./inputs/input.txt"))
