moveScore = 0
moveType = ""
playerChoice = ""
oppChoice = ""
totalScore = 0

def roundStart(opponent, player):
   global moveScore
   moveScore = 0
   #print("Opponent picked " + determineMove(opponent))
   #print("You picked " + determineMove(player))
   #print("It is worth: " + str(scoreLookup(player)) + " points!")
   determineOutcome(opponent, player)
   print ("You scored: " + str(moveScore) + " points")
   return moveScore

def determineOutcome(opponent, player):
    global moveScore
    print(moveScore)
    if player == "X":
        print("You Lose!")
        #A loss adds 0 points 
        if opponent == "A":
            #To lose to rock, go scissors
            moveScore = 3
        elif opponent == "B":
            #To lose to paper, go rock
            moveScore = 1
        elif opponent == "C":
            #To lose to scissors, go paper
            moveScore = 2
    elif player == "Y":
        print("You tied!")   
        #A tie adds 3 points
        if opponent == "A":
         #To tie to rock, go rock
            moveScore = 4
        elif opponent == "B":
         #To tie to paper, go paper
            moveScore = 5
        elif opponent == "C":
         #To tie to scissors, go scissors
            moveScore = 6
    elif player == "Z":
        print("You win!")
        #A win adds 6 points 
        if opponent == "A":
         #To win to rock, go paper
            moveScore = 8
        elif opponent == "B":
         #To win to paper, go scissors
            moveScore = 9
        elif opponent == "C":
         #To win to scissors, go rock
            moveScore = 7

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