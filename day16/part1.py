import re

def solution(filename):
    # read file
    with open(filename, 'r') as fp:
        rawData = fp.read()

    # parsing file
    data = rawData.split('\n\n')
    ticketRulesList = data[0].splitlines()
    # myTicket = data[1].splitlines()[1]  # ignore for now
    nearByTicketsList = data[2].splitlines()[1:]

    # parse ticket rules
    ticketsRE = re.compile('^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')
    ticketRules = {}
    for ticketRule in ticketRulesList:
        mg = ticketsRE.match(ticketRule)
        ruleName = mg[1]
        start1 = int(mg[2]) # first range
        end1 = int(mg[3])
        start2 = int(mg[4]) # second range
        end2 = int(mg[5])

        ticketRules[ruleName] = [
            range(start1, end1 +1),
            range(start2, end2 +1),
        ]

    # parse nearby tickets
    tickets = []
    for ticket in nearByTicketsList:
        tickets.append([int(ticketId) for ticketId in ticket.split(',')])

    # look for invalid tickets
    errorValues = []
    for ticket in tickets:
        for value in ticket:
            for ruleName, (range1, range2) in ticketRules.items():
                if (value in range1) or (value in range2):
                    break
            else:
                errorValues.append(value)

    return sum(errorValues)


if __name__ == "__main__":
    print(solution("./example1.txt"))   # 71
    print(solution("./input.txt"))
