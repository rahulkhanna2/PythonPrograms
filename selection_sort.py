alist = [8 , 12 , 45 , 58 , 22 , 18 , 43 , 30]

def selection(x):
    for i in range(len(x)):
        least = i # Used to save the index of the number to be replaced
        for k in range(i+1 , len(x)): #Used for checking the min number in the list
            if x[k]< x[least]:
                least = k #Picks up the Index of the min number
                print "Least Number found is:",x[least]
        x[least] ,x[i] = x[i], x[least] #swappping of variables
        print 'Value of x is: ',x 
    return x

print selection(alist)
