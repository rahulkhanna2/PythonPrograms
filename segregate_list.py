#Segregate 0s and 1s in array
#input [0,0,1,1,1,1,0,1,1,0]
#output[0,0,0,0,1,1,1,1,1,1]


arr = [0,0,1,1,1,1,0,1,1,0]

count= 0
# ls  = []

#Count total number of zeros
for i in arr:
    if i == 0:
        count +=1

#Change zeros or one's accordingly to the list 
for i in range(0,len(arr)):
    if count >0:
        arr[i] = 0
        count -= 1
    else:
        arr[i] = 1

## USES ONE MORE DATA STRUCTURE APPROACH        
##while x <(len(arr)-count):
##    if  count >0:
##        ls.append(0)
##        count -=1
##    else:
##        ls.append (1)
##    x +=1
##
##print ls

print arr
