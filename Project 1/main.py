import random

def roll():
    min_value=1
    max_value=6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players=input("Enter a number of player 2-4: ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
    else:
        print("Invalid Try again")

max_score = 50
player_score=[0 for _ in range(players)]

while max(player_score) < max_score:

    for player_index in range(players):
        print("\n Player",player_index+1,"turn has just started!\n")
        current_score =0

        while True:
            should_roll =input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value ==1:
                print("You rolled a 1 Turn done!")
                current_score=0
                break
            else:
                current_score += value
                print("You rolled a:",value)

                print("Your score is ", current_score)

        player_score[player_index] +=current_score
        print("Your total Score is :",player_score[player_index])
