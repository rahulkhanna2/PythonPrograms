a= int(raw_input("Enter the height of the tower: "))
def mario(x):
    i = x-1
    for k in range(2,x+2):
        print  " "*(i) + "#"*k
        i = i-1

mario(a)
