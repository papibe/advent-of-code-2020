def solution(filename, preambleSize):
    # read file
    with open(filename, 'r') as fp:
        rawData = fp.read().splitlines()

    data = [int(number) for number in rawData]
    preamble = data[:preambleSize]

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


if __name__ == "__main__":
    print(solution("./example1.txt", 5))    # 127
    print(solution("./input.txt", 25))
