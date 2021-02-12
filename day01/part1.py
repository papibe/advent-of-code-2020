def solution(filename):
    with open(filename) as fp:
        rawData = fp.readlines()

    # convert raw data to integer
    data = [int(line) for line in rawData]

    # Memoization style loop. However, there's no need
    # for memo as data itslef works as memo.
    for n in data:
        diff = 2020 - n
        if diff in data:
            return n * diff

if __name__ == "__main__":
    result = solution("./example.txt")
    print(result)

    result = solution("./input.txt")
    print(result)
