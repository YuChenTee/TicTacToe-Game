import random

#initialize lists to store player and computer moves
list= [["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]]
chosen_list = []
player_list = []
computer_list = []

# to create a list to store all winning combos
win_list = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
            [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
            [[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]

# create log file
movecount = 0
f = open("tictactoe_log.txt" ,"a")

#to print the gameboard by using the contents in the list
def gameboard():
    print(f"""
    {list[0][0]} | {list[0][1]} | {list[0][2]}
    {list[1][0]} | {list[1][1]} | {list[1][2]}
    {list[2][0]} | {list[2][1]} | {list[2][2]}
    """)

#to get player move, check if player move is valid, and append player move into player_list and chosen_list
def player_move():
    print(" It is your turn! ")
    while True:
        row = int(input("Please select row(1-3): "))
        column = int(input("Please select column(1-3): "))
        user_move = [row - 1, column - 1]

        if row >3 or row<1 or column>3 or column<1:
            print("Please select a number between 1 and 3 ! ")

        elif user_move in chosen_list:
            print("Box has already been chosen, please select new move!")

        else:
            list[user_move[0]][user_move[1]] = "X"
            player_list.append(user_move)
            chosen_list.append(user_move)
            global movecount
            movecount+=1
            f.write(f"{movecount},H,{row},{column},X\n")
            gameboard()
            break

# to get computer move by using random, intercept player winning move and check for computer winning move, and append move into computer_list and chosen_list
def computer_move():
    print("Computer is selecting move.....")
    while True:
        row = random.randint(0,2)
        column = random.randint(0,2)
        random_list = [row,column]
        if random_list not in chosen_list:
            move = random_list
            break

    for combo in win_list:
        win_value = 0
        loss_value = 0
        for i in range(0,3):
            if combo[i] in computer_list:
                win_value +=1
            if combo[i] in player_list:
                win_value-=1
        if win_value ==1:
            for i in range(0,3):
                if combo[i] not in chosen_list:
                    move = combo[i]

    for combo in win_list:
        loss_value = 0
        for i in range(0,3):
            if combo[i] in player_list:
                loss_value +=1
        if loss_value ==2:
            for i in range(0,3):
                if combo[i] not in chosen_list:
                    move = combo[i]
    for combo in win_list:
        win_value = 0
        for i in range(0, 3):
            if combo[i] in computer_list:
                win_value+=1
        if win_value == 2:
            for i in range(0,3):
                if combo[i] not in chosen_list:
                    move = combo[i]

    list[move[0]][move[1]] = "O"
    computer_list.append(move)
    chosen_list.append(move)
    gameboard()
    global movecount
    movecount+=1
    f.write(f"{movecount},C,{move[0]+1},{move[1]+1},O\n")

# to determine winner of the game by checking if a winning combo has appeared in computer or player list, and if no winner appears show that its a tie
def win():
    for combo in win_list:
        if combo[0] in player_list and combo[1] in player_list and combo[2] in player_list:
            print("You win!")
            return True

        elif combo[0] in computer_list and combo[1] in computer_list and combo[2] in computer_list:
            print("Computer wins!")
            return True

    if len(chosen_list) == 9:
        print("Its a tie!")
        return True

# Game Loop

#to print game intructions
print("""
WELCOME TO PLAYER VS COMPUTER TIC TAC TOE
Tips: Player who first place his move in 3 consecutive boxes, either horizontally, vertically or diagonally will win the game !
Your piece is X, computer piece is O.
Please select row(1-3) and column(1-3) to place your move !
""")

#to check if who is starting to game
starting_player = input("Would you like to start first? {Y/N} ")
gameboard()

while True:
    if starting_player.upper() == "Y":
        player_move()
        if win() == True:
            break
        computer_move()
        if win() == True:
            break

    elif starting_player.upper() == "N":
        computer_move()
        if win() == True:
            break
        player_move()
        if win() == True:
            break

f.close()





