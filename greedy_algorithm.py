a = int(raw_input("Enter the change you want: "))
def greedy(x):
    count = 0
    while x>0:
        if x>25:
            x = x-25
            count+=1
            continue;
        if x<25 and x>10:
            x = x-10
            count+=1
            continue;
        if x<10 and x>5:
            x = x-5
            count += 1
            continue;
        if x<5 and x>1:
            x = x-1
            count+=1
            continue;
    return count

print greedy(a)
