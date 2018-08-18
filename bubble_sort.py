x = [8,6,9,3,1,0]

def bubble(x):
    print "The original list is: " , x
    i = 0
    while i < len(x):
        for a in range(len(x)-1): #len(x)-1 so that indexes don't go out of range
            if x[a]>x[a+1]:
                x[a] , x[a+1] = x[a+1],x[a]
                """temp = x[a]
                x[a] = x[a+1]
                x[a+1]=temp"""
                print "Value of the list is: " , x
        i += 1
    return x

print bubble(x)
