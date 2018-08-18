# Paste your code into this box
def average(list):
    avg = sum(list) / len(list)
    return avg

def main_func():
    print "Please think of a number between 0 to 100"
    hi = 100
    lo = 0
    number =  average(range(0,101))
    print number
    while True:
        user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if user_input == "l":
            lo = number
            number = average(range(number,hi+1))
            print ("Is your secret number %d ?" %number)
        if user_input == "h":
            hi = number
            number = average(range(lo,number+1))
            print ("Is your secret number %d ?"%number)
        if user_input == "c":
            print "\nGame Over your secret number was " ,number
            break;
        else:
            print "Sorry, I did not understand your input."
            continue;

main_func()
