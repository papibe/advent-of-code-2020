import re
import itertools

def solution(filename):
    SIMPLE = 'S'
    MULTIPLE = 'M'
    LEAF = 'L'

    def getLines(filename):
        with open(filename, 'r') as fp:
            rawData = fp.read()
        data = rawData.split('\n\n')

        rawRules = data[0].splitlines()
        messages = data[1].splitlines()

        return rawRules, messages

    def parseSubRule(s):
        # simple rule
        if '"' in s:
            return { 'type': LEAF, 'value': s[1] }

        # simple rule
        if '|' not in s:
            return {
                'type': SIMPLE,
                'subrules': [int(subrule) for subrule in s.split()]
            }

        # multiple rule
        return {
            'type': MULTIPLE,
            'subrules': [[int(subrule) for subrule in sub.split()] for sub in s.split('|')]
        }


    def parseRules(rules):
        ruleRE = re.compile('^(\d+): (.*)$')

        rules = {}
        for rawRule in rawRules:
            mg = ruleRE.match(rawRule)
            n = mg[1]
            rules[int(n)] = parseSubRule(mg[2])

        return rules


    memo = {}

    def generateWords(n, ast):
        prefix = '  ' * n
        if n in memo:
            return memo[n]

        node = ast[n]
        if node['type'] == LEAF:
            memo[n] = [node['value']]
            return [node['value']]

        words = []
        if node['type'] == SIMPLE:
            retStrings = []
            for subrule in node['subrules']:
                values = generateWords(subrule, ast)
                retStrings.append(values)

            combinations = list(itertools.product(*retStrings))

            final = []
            for combo in combinations:
                final.append([''.join(item) for item in combo])
            memo[n] = final
            return final


        if node['type'] == MULTIPLE:
            allStrings = []
            for options in node['subrules']:

                retStrings = []
                for subrule in options:
                    values = generateWords(subrule, ast)
                    retStrings.append(values)

                combinations = list(itertools.product(*retStrings))

                final = []
                for combo in combinations:
                    final.append([''.join(item) for item in combo])

                allStrings.extend(final)

            memo[n] = allStrings
            return allStrings


    # main ---------------------------------------------------------------------
    rawRules, messages = getLines(filename)
    ast = parseRules(rawRules)  # abstract syntax tree

    splitValidWords = generateWords(0, ast)
    validWords = []
    for words in splitValidWords:
        validWords.append(''.join(words))

    validMSG = 0
    for message in messages:
        if message in validWords:
            validMSG += 1

    return validMSG


if __name__ == "__main__":
    print(solution("./inputs/example1.txt"))    # 2
    print(solution("./inputs/input.txt"))
