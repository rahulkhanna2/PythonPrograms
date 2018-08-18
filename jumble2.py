import string
import random
import enchant

GB = enchant.Dict("en_GB")
US = enchant.Dict("en_US")
given_letters = []
user_list = []
final_dic = {}
lett = "tnhrdlcwfgybxyz"
vowels  = "aeiouspcdmae"
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


print "--------------------- Rules Of the game -----------------------"
print """ \n Each Player will get 3 chances in which player will be given
 some letters. Player has to make words from the letters
 given. Enter 'n' to get more letters.
 \n
 NOTE:- The number of times new letters added are only 3."""
print "--------------------- Rules Of the game -----------------------"


def scrabble_score(word):
    total  = 0
    word = word.lower()
    for words in word:
        key = words
        total  += score[key]
    final_dic[word] = total   #Sums the total Value and adds it to list


def input_from_user():
    want_to_end = True
    while want_to_end:
        user_in = raw_input("Enter your word: ").lower()
        if len(user_in)>1:
            check_alphabets(user_in)
        if user_in == "s":
            print "Your letters are:  " + ' '.join([str(item) for item in given_letters])
            continue;
        if user_in == "n":
            want_to_end = False
        elif len(user_in) <=1:
            print "---- PLEASE ENTER A WORD ----"
            continue;


def check_alphabets(the_word):
    if GB.check(the_word) and US.check(the_word):
        if the_word not in final_dic:
            #Check if letters are in the given list
            if all(i in given_letters for i in the_word):
                scrabble_score(the_word)
                user_list.append(the_word)
            else:
                print "---- Please use only the LETTERS given ----"
        else:
            print "---- Word already in the list.!! -----"
    else:
        print "------ PLEASE ENTER A VALID WORD -------"

def append_alphabets():
        x = 0
        while x <= 2:
          y = random.choice(lett)
          b = random.choice(vowels)
          given_letters.append(y)
          given_letters.append(b)
          x += 1
        print  "Your new letters are:  " + ' '.join([str(item) for item in given_letters])

        
def final_func():
    for i in range(3):
        append_alphabets()
        input_from_user()

final_func()


print "\nYour created words were: " , (final_dic)
print "\nTotal words created were: ", len(final_dic)
print "\nYour total score is:  " , sum(final_dic.values())
raw_input("\nPress Enter to Exit.")
