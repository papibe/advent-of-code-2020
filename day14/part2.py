import re

def solution(filename):

    def binString(n):
        return f'{n:036b}'


    def applyMask(address, smask):
        bitadrres = binString(address)
        newaddr = []
        xPositions = []

        # for i in range(36):
        for i, bit in enumerate(smask):
            # keep same value
            if bit == '0':
                newaddr.append(bitadrres[i])

            # force a 1
            if bit == '1':
                newaddr.append('1')

            # floating: mark with X and save the position
            if bit == 'X':
                newaddr.append('X')
                xPositions.append(i)

        return (xPositions, newaddr)


    # main ---------------------------------------------------------------------
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

        # line is a mem instruction
        if memMG is not None:
            address = int(memMG[1])
            value = int(memMG[2])

            xPositions, floating = applyMask(address, mask)

            # floating address
            if xPositions:
                possibleFloatingAddresses = 2**len(xPositions)
                for address in range(possibleFloatingAddresses):
                    bitAddress  = "{:0{l}b}".format(address,l=(len(xPositions)))
                    for i, bit in enumerate(bitAddress):
                        floating[xPositions[i]] = bit

                    memory[''.join(floating)] = value
            else:
                # no Xs in the mask: regular address
                memory[''.join(floating)] = value

    return sum(memory.values())


if __name__ == "__main__":
    print(solution("./inputs/example2.txt"))   # 208
    print(solution("./inputs/input.txt"))
