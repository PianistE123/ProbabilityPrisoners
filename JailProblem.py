
selection = [[0,0],[0,1],[1,0],[1,1]]

choise1 = 0
choise2 = 0


def firstStrategy(pair):
    if pair[0] == 1:
        return 0
    else:
        return 1

def secondStrategy(pair):
    if pair[0] == 0 and pair[1] == 1:
        return 1
    else:
        return 0

allSituations = 16
successes = 0

for i in range(4):
    for j in range(4):
        choice1 = firstStrategy(selection[i])
        choice2 = secondStrategy(selection[j])
        if selection[j][choice1] == selection[i][choice2]:
            successes += 1

print("If they took righht strategies:")
print("successes: ", successes)
Probability = successes/allSituations
print("P = ",Probability)


allSituations = 16
successes = 0

for i in range(4):
    for j in range(4):
        choice1 = secondStrategy(selection[i])
        choice2 = firstStrategy(selection[j])
        if selection[j][choice1] == selection[i][choice2]:
            successes += 1

print("If they took each others strategies:")
print("successes: ", successes)
Probability = successes/allSituations
print("P = ",Probability)

successes = 0

for i in range(4):
    for j in range(4):
        choice1 = firstStrategy(selection[i])
        choice2 = firstStrategy(selection[j])
        if selection[j][choice1] == selection[i][choice2]:
            successes += 1

print("If they took the same first strategies:")
print("successes: ", successes)
Probability = successes/allSituations
print("P = ",Probability)

successes = 0

for i in range(4):
    for j in range(4):
        choice1 = secondStrategy(selection[i])
        choice2 = secondStrategy(selection[j])
        if selection[j][choice1] == selection[i][choice2]:
            successes += 1

print("If they took the same second strategies:")
print("successes: ", successes)
Probability = successes/allSituations
print("P = ",Probability)

