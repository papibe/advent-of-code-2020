def solution(filename):
    with open(filename, 'r') as fp:
        rawData = fp.read()

    groups = rawData.split("\n\n")

    total = 0
    for group in groups:
        answersMap = {}
        groupLines = group.splitlines()
        for answer in groupLines:
            for char in answer:
                answersMap[char] = 1 + answersMap.get(char, 0)

        # count how many awswers were responded by all the group
        groupAnswers = [1 for k, v in answersMap.items() if v == len(groupLines)]
        total += len(groupAnswers)

    return total


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 6
    print(solution("./input.txt"))
