def solution(filename):
    with open(filename) as fp:
        rawData = fp.readlines()

    # convert raw data to integer
    data = [int(line) for line in rawData]

    # Memoization style loop. However, there's no need
    # for memo as data itslef works as memo.
    for i, n in enumerate(data):
        for j in range(i, len(data)):
            m = data[j]
            diff = 2020 - n - m
            if diff in data:
                return n * m * diff

if __name__ == "__main__":
    result = solution("./example.txt")
    print(result)

    result = solution("./input.txt")
    print(result)
