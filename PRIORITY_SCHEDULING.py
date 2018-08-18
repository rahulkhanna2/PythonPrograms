n = int(raw_input("Enter the no of processes:\n"))
process= {}
wait_time = 0
w = 0

print "process{priority:burst_time}\n";

for i in range(n):
    var1,var2 = raw_input("Enter the process#"+ str(i+1) + " burst time with its priority:").split()
    var1,var2 = [int(var1),int(var2)]
    process[var2] = var1

for i in sorted(process):
    wait_time +=w
    w +=process[i]
print "Average waiting time is: ",(float(wait_time)/n)
print "Total completiton time: ",w
#print "Total Turnaround time is: ",(float())


raw_input()
