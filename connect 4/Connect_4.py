#Initializing a matrix all values as none
Matrix = []
for i in range(6):
    x = []
    for j in range(7):
        x.append(None)
    Matrix.append(x)

# To display Matrix
def display(Matrix):
    print("\n")
    for i in range(6):
         print(Matrix[i])

#To update the display and add entry to it
def updatedisplay(num, player):
    column = Matrix[num]
    index = None
    for i in range(len(Matrix)-1,-1,-1):
        if Matrix[i][num] == None:
            if player == 1:
                Matrix[i][num]=' X '
            else:
                Matrix[i][num]=' O '
            display(Matrix)
            return True
    return False

#check if there is a winner
def check_win(Matrix, player):
    # Checking in row
    for j in range(len(Matrix[0]) - 3):
        for i in range(len(Matrix)):
            if Matrix[i][j] == player and Matrix[i][j + 1] == player and Matrix[i][j + 2] == player and Matrix[i][
                j + 3] == player:
                return True

    # checking in column
    for i in range(len(Matrix[0])):
        for j in range(len(Matrix) - 3):
            if Matrix[j][i] == player and Matrix[j + 1][i] == player and Matrix[j + 2][i] == player and Matrix[j + 3][
                i] == player:
                return True

    # checking Forward diagnol
    for i in range(len(Matrix[0]) - 3):
        for j in range(len(Matrix) - 3):
            if Matrix[j][i] == player and Matrix[j + 1][i + 1] == player and Matrix[j + 2][i + 2] == player and \
                    Matrix[j + 3][i + 3] == player:
                return True

    # checking Backward diagnol
    for i in range(len(Matrix[0]) - 3):
        for j in range(3, len(Matrix)):
            if Matrix[j][i] == player and Matrix[j - 1][i + 1] == player and Matrix[j - 2][i + 2] == player and \
                    Matrix[j - 3][i + 3] == player:
                return True
    return False

#checks if given entry column is valid or not
def isValidMove(column_no):
    if column_no >=1 and column_no <=7:
        return True
    else:
        return False

#the main function in which the game runs
def startgame():
    player = 1
    no_win = True
    winner = ""
    while(no_win):
        ask_column = ('\nPlayer ' + str(player) + ' turn, enter the column number(1-7): ')
        column_no = input(ask_column)
        if column_no:
            column_no = int(column_no)
            if isValidMove(column_no) == False:
                print('Hey, this is not a right move. Try again.\n')
            else:
                flag = updatedisplay(column_no - 1, player)
                if flag:
                    if player == 1:
                        tile = " X "
                    else:
                        tile = " O "
                    if check_win(Matrix,tile):
                        winner = tile
                        no_win = False
                    if player == 1:
                        player = 2
                    else:
                        player = 1

                else:
                    print('Hey, this is not a right move. Try again.\n')
        else:
            print('Hey, this is not a right move. Try again.\n')
    if winner == " X ":
        winner = "1"
    else:
        winner = "2"
    print('THE WINNER IS PLAYER '+ str(winner))

print('Starting Connect 4 Game... Get ready!\n')
display(Matrix)
startgame()
