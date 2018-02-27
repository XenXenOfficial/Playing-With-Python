test = [['1',' ',' ',' '],['2',' ',' ',' '],['3',' ',' ',' ']]

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
    print('   1', ' 2', ' 3')
    for i in range(len(test)):
        for i2 in range(len(test[i])):
            print(test[i][i2], '|' ,end='')
            
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
    while True:
        answer = input("What spot {}? ".format(pVal))
        answer = list(map(int,answer))
        try:
            if test[answer[0] - 1][answer[1]] not in ('x', 'y'):
                if pVal == 'Player One':
                    test[answer[0] - 1][answer[1]] = 'x'
                    if check((answer[0] - 1), (answer[1])) == True:
                        print("Player One winner!")
                        reprint()
                    else:
                        break
                else:
                    test[answer[0] - 1][answer[1]] = 'y'
                    if check((answer[0] - 1), (answer[1])) == True:
                        print("Player Two winner!")
                        reprint()
                    else:
                        break
            else:
                print("Cant do that!")
        except IndexError:
            print("Not a valid spot!")
            continue
