moveScore = 0
moveType = ""
playerChoice = ""
oppChoice = ""
totalScore = 0

def roundStart(opponent, player):
    global moveScore
    moveScore = 0
    print("You picked " + determineMove(player))
    print("It is worth: " + str(scoreLookup(player)) + " points!")
    print("Opponent picked " + determineMove(opponent))
    determineOutcome(opponent, player)
    print ("You scored: " + str(moveScore) + " points")
    return moveScore

def determineOutcome(opponent, player):
    global moveScore
    print(moveScore)
    if player == "X":
        if opponent == "A":
            print("It's a tie!")
            moveScore = moveScore + 3
        elif opponent == "B":
            print("You lose!")
        elif opponent == "C":
            print("You win!")
            moveScore = moveScore + 6
    elif player == "Y":
        if opponent == "A":
            print("You win!")
            moveScore = moveScore + 6
        elif opponent == "B":
            print("It's a tie!")
            moveScore = moveScore + 3
        elif opponent == "C":
            print("You lose!")
    elif player == "Z":
        if opponent == "A":
            print("You lose!")
        elif opponent == "B":
            print("You win!")
            moveScore = moveScore + 6
        elif opponent == "C":
            print("It's a tie!")
            moveScore = moveScore + 3

def determineMove(move):
    if move == "A" or move == "X":
        moveType = "Rock"
    elif move == "B" or move == "Y":
        moveType = "Paper"
    elif move == "C" or move == "Z":
        moveType = "Scissors"
    return moveType


def scoreLookup(score):
    global moveScore
    if score == "A" or score == "X":
        moveScore = 1
    elif score == "B" or score == "Y":
        moveScore = 2
    elif score == "C" or score == "Z":
        moveScore = 3
    return moveScore


with open('input.txt', 'rt') as f:
    for line in f:
        print (line)
        for element in range(0, len(line)):
            playerChoice = line[2]
            oppChoice = line[0]
        roundStart(oppChoice, playerChoice)
        totalScore = totalScore + moveScore
        print (totalScore)

print (totalScore)