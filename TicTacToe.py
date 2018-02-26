test = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def check(x,y):
    if test[0][y] == test[1][y] == test[2][y]:
        return True
    if test[x][0] == test[x][1] == test[x][2]:
        return True
    if x == y and test[0][0] == test[1][1] == test[2][2]:
        return True
    if x + y == 2 and test[0][2] == test[1][1] == test[2][0]:
        return True
    return False
def reprint():
    for i in range(len(test)):
        for i2 in range(len(test[i])):
            print('|',test[i][i2], '|', end='',)
        print()
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
    if pVal == 'Player One':
        while True:
            answer = input("What one {}? ".format(pVal))
            answer = list(map(int,answer))
            if test[answer[0] - 1][answer[1] - 1] not in ('x', 'y'):
                test[answer[0] - 1][answer[1] - 1] = 'x'
                if check((answer[0] -1), (answer[1] -1)) == True:
                    print("Player One winner!")
                    reprint()
                else:
                    break
            else:
                print("Can't do that!")
                continue
    else:
        while True:
            answer = input("What one {}? ".format(pVal))
            answer = list(map(int,answer))
            if test[answer[0] - 1][answer[1] - 1] not in ('x','y'):
                test[answer[0] - 1][answer[1] - 1] = 'y'
                if check((answer[0] -1), (answer[1] -1)) == True:
                    print("Player Two winner!")
                    reprint()
                else:
                    break
            else:
                print("Cant do that!")
                continue
