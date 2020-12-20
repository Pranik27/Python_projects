# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:46:15 2020

@author: PRANIKP

Create a Tic Tac Toe game.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol 
on the board


"""

print("WELCOME to the TIC TAC TOE GAME!!!")
print("Baord numbering system as explained below!! \n")
print(" 7|8|9")
print("--------")
print(" 4|5|6")
print("--------")
print(" 1|2|3\n")



##################################################################################################3
#Fuction to print the board 
def print_board(board):
    print(" {}|{}|{}".format(board[7],board[8],board[9]))
    print("--------")
    print(" {}|{}|{}".format(board[4],board[5],board[6]))
    print("--------")
    print(" {}|{}|{} \n".format(board[1],board[2],board[3]))

    

##############################################################################################
#Function to decide which player goes first based on the sign selection
def select_x_o():
    player_1_sign = input("Player 1 - please select 'X' or 'O' : ")
    
    sign = False
    
    while not sign:
        if(player_1_sign == 'X' or player_1_sign == 'O'):
            sign = True
        else:
            print("{} entered is not correct . Please select 'X' or 'O'".format(player_1_sign))
            player_1_sign = input("Player 1 - please select 'X' or 'O' : ")

#Selecting which player will go first
    
    if(player_1_sign == 'X'):
        print("Player 1 : You will go first\n")
        return ('X','1')
    else:
        print("player 2 : you will go first \n")
        return ('O','2')



#############################################################################################
#Chceknig if any player won
def check_win(ply1_horz,ply2_horz):
    horz1 = {'1','2','3'}
    horz2 = {'4','5','6'}
    horz3 = {'7','8','9'}
    
    vert1 = {'1','4','7'} 
    vert2 = {'2','5','8'}
    vert3 = {'3','6','9'}
    
    diag1 = {'1','5','9'}
    diag2 = {'3','5','7'}
    
    
    if ((horz1.issubset(ply1_horz)) or (horz2.issubset(ply1_horz)) or (horz3.issubset(ply1_horz))):
        print("CONGRATZZ !! Player 1 . YOU WON !!")
        return True
    elif((vert1.issubset(ply1_horz)) or (vert2.issubset(ply1_horz)) or (vert3.issubset(ply1_horz))):
        print("CONGRATZZ !! Player 1 . YOU WON !!")
        return True
    elif((diag1.issubset(ply1_horz)) or (diag2.issubset(ply1_horz))):
        print("CONGRATZZ !! Player 1 . YOU WON !!")
        return True
    elif ((horz1.issubset(ply2_horz)) or (horz2.issubset(ply2_horz)) or (horz3.issubset(ply2_horz))):
        print("CONGRATZZ !! Player 2 . YOU WON !!")
        return True
    elif((vert1.issubset(ply2_horz)) or (vert2.issubset(ply2_horz)) or (vert3.issubset(ply2_horz))):
        print("CONGRATZZ !! Player 2 . YOU WON !!")
        return True
    elif((diag1.issubset(ply2_horz)) or (diag2.issubset(ply2_horz))):
        print("CONGRATZZ !! Player 2 . YOU WON !!")
        return True
    
    return False



#############################################################################################
#To check if it's a draw
def check_draw(val1,val2):
    
    if((len(val1)== 4) and (len(val2)== 5)):
        print("GAME IS DRAWN!!")
        return True
    elif((len(val2)== 4) and (len(val1)== 5)):
        print("GAME IS DRAWN!!")
        return True
        
    return False

    


##########################################################################################
#Function will keep on the game
def game_on(inp_move):
    
    in_progress = True
    move = inp_move[0]
    player_number = inp_move[1]
    ply1_horz = set()
    ply2_horz = set()
    
    while(in_progress):
        current_pos = user_input(move,player_number)
        if(move == 'X'):
            move = 'O'
        else:
            move = 'X'
        
        if(player_number == '1'):
            player_number = '2'
            ply1_horz.add(current_pos)
        else:
            player_number = '1'
            ply2_horz.add(current_pos)
        
        if (check_win(ply1_horz,ply2_horz)):
            break
        
        if (check_draw(ply1_horz,ply2_horz)):
            break




####################################################################################################
#validates user input and updates the board
def user_input(move,player_number):
    global board
    global dummy_list
    
    
    print("Player {}:".format(player_number))
    val_input = input("choose your next position [1-9]: ")
    
    while (val_input.isdigit() == False):
        print("{} does not lie between [1-9]. Please select valid number \n".format(val_input))
        print("Player {}:".format(player_number))
        val_input = input("choose your next position [1-9]: ")
           
    
    if (int(val_input) in range(1,10)):
        if(val_input not in dummy_list):
            board[int(val_input)] = move
            dummy_list.append(val_input)
        else:
            print("{} position is already selected . Please select vacant position!!\n".format(int(val_input)))
    else:
        print("Please provide a valid position : [1-9]\n")

        
    print_board(board)
    return (val_input)



######################################################################################
#Ask if want to play again
def play_again():
    
    result = input("Do you want to play again? 'Y' or 'N': ")
    
    if (result == 'Y'):
        return True
    else:
        return False

#####################  MAIN LOGIC ###################################


play_ahead = True

while (play_ahead):
    board = ['DUMMY',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    dummy_list = []
    print_board(board)
    inp_move = select_x_o()
    game_on(inp_move)
    play_ahead = play_again()
    




