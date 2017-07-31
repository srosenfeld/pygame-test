import pprint
import random

theBoard = {
 'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print("-----")
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print("-----")
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def playerMove(symbol):
    print("What is your move?")
    move = input()
    theBoard[move] = symbol
    printBoard(theBoard)
    print("\n \n \n")

def computerMove(symbol):
    optionList = []
    for k,v in theBoard.items():
        if v == ' ':
            optionList.append(k)
    move = optionList[random.randint(0, (len(optionList)-1))]
    theBoard[move] = symbol
    printBoard(theBoard)
    print("\n \n \n")

print("Would you like to be 'X' or 'O'?")
p1 = input().upper()
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'
            
    
printBoard(theBoard)
playerMove(p1)
computerMove(p2)
playerMove(p1)
computerMove(p2)
playerMove(p1)
computerMove(p2)
