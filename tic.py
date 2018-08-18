import random

board = [0,1,2,
         3,4,5,
         6,7,8,]

def show():
    print board[0] , "|" , board[1] , "|" , board[2]
    print "----------"
    print board[3] , "|" , board[4] , "|" , board[5]
    print "----------"
    print board[6] , "|" , board[7] , "|" , board[8]

show()


def checkLine(char , spot1 , spot2, spot3):
            if board[spot1] == char and board[spot2] == char and board[spot3] == char:
                return True


def checkAll(char):
    if checkLine(char, 0,1,2):
        return True
    if checkLine(char, 3,4,5):
        return True
    if checkLine(char, 6,7,8):
        return True
    if checkLine(char, 0,3,6):
        return True
    if checkLine(char, 1,4,7):
        return True
    if checkLine(char, 2,5,8):
        return True
    if checkLine(char, 2,4,6):
        return True
    if checkLine(char, 0,4,8):
        return True



while True:
    try:
            input = int(raw_input("Select your spot: "))
            if board[input]!= "X" and board[input]!= "O":
                board[input]  = "X"
                #Check for the winnig condition
                if checkAll("X") == True :
                    show()
                    print "\n_____ Congratulations !!! X Wins ____"
                    break;  
##            elif board[input] == "O":
##                while True:
##                    print "Please Choose another spot. "
##                    input = int(raw_input("Select your spot"))
##                    board[input] = "X"
##                    break;

            opponent  = random.randint(0,8)
            if board[opponent] != "O" and board[opponent] != "X":
                    board[opponent]  = "O"
##            elif board[opponent] == "X" : # check for the necessary condition whether there is already placed or not
##                opponent = random.randint(0,8)
##                board[opponent] = "O"
                 # Here it is problem not giving the right output complete row is of O

                            #Check for the winning condition
                    if checkAll("O") == True :
                        show()
                        print " \n____ O Wins _____"
                        break;

                
            else:
               print "Sorry choose another spot"

            show()
    except ValueError:
        continue;
