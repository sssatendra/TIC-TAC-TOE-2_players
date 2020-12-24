import random
x

def display_broad(board):
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("---------")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("---------")
    print(board[7]+" | "+board[8]+" | "+board[9])

#test=[" ","X","O","X","O","X","O","X","O","X"] 

def player_inp():
    mark=" "
    while mark!="X" and mark!="O":
        mark=input("Player 1 select either X or O: ")
        mark=mark.upper()
    player1=mark

    if player1=="X":
        player2="O"
    else:
        player2="X"

    return (player1,player2)


#de

def placemarker(board,mark,position):
    board[position]=mark

#placemarker(test,"$",8)
#display_broad(test)

def win_check(board,mark):
    # ROWS Check , columns and diagonals check
    return board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or board[1]==board[5]==board[7]==mark or board[3]==board[5]==board[7]==mark

#win_check(test,"X")

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):
    return board[position]==" "

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board full
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter the Position 1 to 9:  "))
    return position

def reply():
    choice=input("Do you want to play again, Enter Yes or No : ")

    return choice

print("Welcome to TIC TAC TOE")



while True:
    the_board=[" "]*10
    player1_marker,player2_marker=player_inp()
    turn=choose_first()
    print(turn+"  will play first")
    play_game=input("ready to play y or n: ")
    play_game=play_game.lower()

    if play_game=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='Player 1':
            display_broad(the_board)
            position=player_choice(the_board)
            placemarker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_broad(the_board)
                print("player 1 won the game")
                game_on=False
            else:
                if full_board(the_board):
                    display_broad(the_board)
                    print("TIE Game")
                    break
                else:
                    turn="Player 2"

        else:

            display_broad(the_board)
            position=player_choice(the_board)
            placemarker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_broad(the_board)
                print("player 2 won the game")
                game_on=False
                
            else:
                if full_board(the_board):
                    display_broad(the_board)
                    print("TIE Game")
                    break
                else:
                    turn="Player 1"


    if not reply():
        break
                    


