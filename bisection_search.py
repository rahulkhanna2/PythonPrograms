x= 25
epsilon = 0.01
low  = 0
high = x
ans = (low + high)/2.0
while abs(ans**2 -x) >= epsilon:
    print "VALUE OF ABS IS: ", (abs(ans**2-x))
    print ('low = ' + str(low)+ " " + "high: " + str(high) + "  ans: " + str(ans))
    if (ans**2)< x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print "The ans is: ", ans
