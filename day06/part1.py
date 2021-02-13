def solution(filename):
    with open(filename, 'r') as fp:
        rawData = fp.read()

    groups = rawData.split("\n\n")

    total = 0
    for group in groups:
        answersMap = {}
        for answer in group.split('\n'):
            for char in answer:
                answersMap[char] = True

        groupAnswers = len(answersMap)  # size of the dictionary
        total += groupAnswers

    return total


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 11
    print(solution("./input.txt"))
