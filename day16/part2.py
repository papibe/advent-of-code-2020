import re

def solution(filename):
    # read file
    with open(filename, 'r') as fp:
        rawData = fp.read()

    # parsing file
    data = rawData.split('\n\n')
    ticketRulesList = data[0].splitlines()
    myTicketRaw = data[1].splitlines()[1]
    nearByTicketsList = data[2].splitlines()[1:]

    # parse ticket rules -------------------------------------------------------
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

    # parse my ticket
    myTicket = [int(s) for s in myTicketRaw.split(',')]

    # parse nearby tickets -----------------------------------------------------
    tickets = []
    for ticket in nearByTicketsList:
        tickets.append([int(ticketId) for ticketId in ticket.split(',')])

    # get valid tickets
    validTickets = []
    for ticket in tickets:
        countInRange = 0
        for value in ticket:
            for ruleName, (range1, range2) in ticketRules.items():
                if (value in range1) or (value in range2):
                    countInRange += 1
                    break
        if countInRange == len(ticketRules):
            validTickets.append(ticket)

    # initialize counting object
    tries = [{} for _ in myTicket]

    for ticket in validTickets:
        for i, value in enumerate(ticket):
            for ruleName, (range1, range2) in ticketRules.items():
                if (value in range1) or (value in range2):
                    tries[i][ruleName] = 1 + tries[i].get(ruleName, 0)

    # resolving field names in my ticket
    finalTicket = {}
    nrules = len(ticketRules)
    while len(finalTicket) != nrules:
        for i, trie in enumerate(tries):
            count = 0
            for rule in trie:
                if rule not in ticketRules:
                    continue
                if trie[rule] == len(validTickets):
                    count += 1
                    candidate = {'field': i, 'rule': rule}
            # exactly one matched rule
            if count == 1:
                finalTicket[candidate["rule"]] = candidate["field"]
                del ticketRules[candidate['rule']]

    # multiply values that start with departure
    product = 1
    for name, field in finalTicket.items():
        if name.startswith('departure'):
            product *= myTicket[field]

    return product


if __name__ == "__main__":
    print(solution("./input.txt"))
