import re
import itertools
from copy import deepcopy

def solution(filename, patch=False):
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


    def _matchRule(msg, index, ast, ruleStack):
        if (len(msg) - index) < len(ruleStack):
            return False

        if (index == len(msg)) or len(ruleStack) == 0:
            return len(ruleStack) == 0 and (index == len(msg))

        rule = ast[ruleStack.pop()]
        if rule['type'] == LEAF:
            if msg[index] == rule['value']:
                return _matchRule(msg, index + 1, ast, ruleStack[:])

        elif rule['type'] == SIMPLE:
            newRuleStack = ruleStack[:]
            newRuleStack.extend(list(reversed(rule['subrules'])))
            if _matchRule(msg, index, ast, newRuleStack):
                return True

        elif rule['type'] == MULTIPLE:
            for mulRule in rule['subrules']:
                newRuleStack = ruleStack[:]
                newRuleStack.extend(list(reversed(mulRule)))
                if _matchRule(msg, index, ast, newRuleStack):
                    return True

        return False


    def matchRule(msg, index, ast):
        rule = ast[0]

        if rule['type'] == SIMPLE:
            if _matchRule(msg, index, ast, list(reversed(rule['subrules']))):
                return True

        elif rule['type'] == MULTIPLE:
            for mulRule in rule['subrules']:
                if _matchRule(msg, index, ast, list(reversed(mulRule))):
                    return True

        return False


    # main ---------------------------------------------------------------------
    rawRules, messages = getLines(filename)
    ast = parseRules(rawRules)  # abstract syntax tree

    # patching for part2
    if patch:
        ast[8] = {
            'type': MULTIPLE,
            'subrules': [[42], [42, 8]]
        }
        ast[11] = {
            'type': MULTIPLE,
            'subrules': [[42, 31], [42, 11, 31]]
        }

    validMSG = 0
    for message in messages:
        if matchRule(message, 0, ast):
            validMSG += 1

    return validMSG


if __name__ == "__main__":
    # part 1
    print(solution("./inputs/example1.txt"))    # 2
    print(solution("./inputs/input.txt"))

    # part 2
    print(solution("./inputs/example2.txt", patch=True))    # 12
    print(solution("./inputs/input.txt", patch=True))
