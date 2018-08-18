#Nagarro Bootcamp Question. Check and remove duplicate



a = [3,5,1,2,4]
b = [9,3,4,5,1,22,2]

##a = [1,1,1]
##b = [1,1,1,1,1]

##a = [1,2,2,3]
##b = [2,3,6,1,2,2]

if len(a)<len(b):
    for i in a:
        if i in b:
            b.remove(i)
            

print b
