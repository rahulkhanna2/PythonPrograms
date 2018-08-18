s,t = map(int,raw_input().split(" "))
a,b = map(int,raw_input().split(" "))
m,n = map(int,raw_input().split(" "))
apple = map(int, raw_input().split(" "))
orange = map(int, raw_input().split(" "))
total_apples = total_oranges = 0

for x in apple:
    if (x+a)>=s and (x+a)<=t:
        total_apples +=1
for i in orange:
    if (i+b)>=s and (i+b)<=t:
        total_oranges +=1

print total_apples
print total_oranges

    
