import math # did this even work i am very new
totalfish = 50

num_teams = int(input("How many teams:"))
fishes = [0 for _ in range(num_teams)]

EXPLOIT = 1
LIMIT = 2
REPLENISH = 3
REPORT = 4

num_rounds = 20

for r in range(num_rounds):
    actions_this_round = []
    print(f"Start round {r}")
 
    for team in range(1, num_teams + 1):
        action = int(input(f"Enter action for team {team}:"))
        actions_this_round.append(action)
    print(f"Actions this round = {actions_this_round}\n")

    someone_reporting = any(act == REPORT for act in actions_this_round)
    someone_exploiting = any(act == EXPLOIT for act in actions_this_round)
    exploit_bounty = totalfish / 20
    limit_bounty = totalfish / 50
    report_bounty = sum(act == EXPLOIT for act in actions_this_round) * 2 // sum(act == REPORT for act in actions_this_round)
    # not sure how to better represent report_bounty
    # gonna figure out how to import ceil from math later, guh

    for team in range(num_teams):
        if actions_this_round[team] == EXPLOIT:
            if someone_reporting:
                 fishes[team] -= 2
            else:
                fishes[team] += exploit_bounty
                totalfish -= 2
        if actions_this_round[team] == LIMIT:
            fishes[team] += limit_bounty
            totalfish -= limit_bounty
        if actions_this_round[team] == REPLENISH:
            if someone_exploiting:
                totalfish += 3
            else:
                totalfish += 5
        if actions_this_round[team] == REPORT:
            if someone_exploiting:
                fishes[team] += report_bounty
    for team in range(1, num_teams + 1):
        print(f"Team {team} score = {fishes[team]}\n") #how to get this display correctly, index out of range
                
    

        
