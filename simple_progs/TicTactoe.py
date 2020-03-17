#program for tic tac toe

import sys
import os

import random

#very importand. Keep showing board 

#step 1: user puts x
#step 2: fix something for opponent
#step 3 go for winning condition

#define board

board = []
theboard = ['0','1','2','3','4','5','6','7','8','9']
for i in theboard:
    board.append(i)


def show_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])

show_board()



#check_horiz_char check for horizontal wins

def Check_horiz(char):
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    elif board[3] == char and board[4] == char and board[5] == char:
        return True
    elif board[6] == char and board[7] == char and board[8] == char:
        return True
    else:
        return False
    

def Check_vert(char):

    if board[0] == char and board[3] == char and board[6] == char:
        return True
    elif board[1] == char and board[4] == char and board[7] == char:
        return True
    elif board[2] == char and board[5] == char and board[8] == char:
        return True
    else:
        return False

def Check_rightdiag(char):
    if board[0] == char and board[4] == char and board[8] == char:
        return True
    else:
        return False

def Check_leftdiag(char):
    
    if board[2] == char and board[4] == char and board[6] == char:
        return True
    else:
        return False
    
    


def player_win(char):
    if Check_horiz(char) or Check_vert(char) or Check_leftdiag(char) or Check_rightdiag(char):
        return True
    else:
        return False


##defining the rules of game.
#player puts 'x' and opponent puts 'o'

while True:

    #pinput is player input
    pinput = input("enter your position")

    pinput = int(pinput)

    #now oinput is computer: player 2
    #now choose opponent put's o at random.
    #between the range 0 to 8
    #initialise random number generator

    random.seed()

    oinput = random.randrange(0,8,1)

    #check occupancy of opponent
    

    if board[pinput] != 'x' and board[pinput] != 'o':
        board[pinput] = 'x'

    if board[oinput] != 'x' and board[oinput] != 'o':
        board[oinput] = 'o'

    else:
        print('This spot is already taken')

    #show matrix after every move

    show_board()
    if player_win('x'): 
        print('x wins')
        break
    if player_win('o'):
        print('o wins')

        break
    
    

 


        
    
    
