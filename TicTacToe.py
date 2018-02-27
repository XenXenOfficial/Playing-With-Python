import sys
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def check(x,y):
    if board[0][y] == board[1][y] == board[2][y]:
        return True
    if board[x][0] == board[x][1] == board[x][2]:
        return True
    if x == y and board[0][0] == board[1][1] == board[2][2]:
        return True
    if x + y == 2 and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False
    
def reprint():
    print('    1   2   3')
    for i in range(len(board)):
        print("{} | {} | {} | {} |".format(i+1, board[i][0], board[i][1], board[i][2]))
playerTurn = True

while True:
    pVal = ''
    reprint()
    if playerTurn == False:
        pVal = 'Player Two'
        playerTurn = True
    else:
        pVal = 'Player One'
        playerTurn = False
    while True:
        answer = input("\nWhat spot {}? ".format(pVal))
        answer = list(map(int,answer))
        try:
            if board[answer[0] - 1][answer[1] - 1] not in ('x', 'y'):
                if pVal == 'Player One':
                    board[answer[0] - 1][answer[1] - 1] = 'x'
                    if check((answer[0] -1), (answer[1] -1)) == True:
                        print("Player One winner!")
                        reprint()
                        sys.exit()
                    else:
                        break
                else:
                    board[answer[0] - 1][answer[1] - 1] = 'y'
                    if check((answer[0] -1), (answer[1] -1)) == True:
                        print("Player Two winner!")
                        reprint()
                        sys.exit()
                    else:
                        break
            else:
                print("Cant do that!")
        except IndexError:
            print("Not a valid spot!")
            continue
