x = [20,5,3,9,6,7,90]
#output = [5,1,0,4,2,3,6]

i = 0
a =[]
for i in range(0,len(x)):
    count =0
    for j in range(0,len(x)):
        if x[j]<x[i]:
            count +=1
    a.append(count)

print a
