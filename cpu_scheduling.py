n = int(raw_input("Enter the no of processes:\n"))
ls = []
wait_time = 0
w = 0

for i in range (0,n):
    x= int(raw_input("Enter the time for process#" + str(i)+ "\n"))
    ls.append(x)

def FCFS():
    global wait_time
    global w
    for j in range(n):
        wait_time += w
        w += ls[j]
    return w, wait_time


def SJF():
    ls.sort()
    global wait_time
    global w
    for j in range(n):
        wait_time += w
        w += ls[j]
    return w,wait_time


decide = int(raw_input("Which algorithm you want to choose:\n1. First Come First Serve\n2.Shortest Job First\n"))

if decide == 1:
    FCFS()
else:
    SJF()

print "Total completion time is:", w
print "Average waiting time is: %f" %(wait_time/n)
