# Binary addition of numbers using just a for loop




import time
n = int(raw_input("ho many numbers you want to enter: "))
ls = []
result = []
for i in range(n):
    x = (raw_input("enter your number: "))
    ls.append(x)

start_time = time.time()

for j in ls:
    j = j[::-1] #reverse the string for easy calculation

    power = 0
    total = 0

    for number in j:
        total += int(number) * (2**power)
        power += 1

    result.append(total)

print '\nThe total sum is %d '%(sum(result))


end_time = time.time()

print "This algorithm took %f seonds" %(end_time-start_time)

raw_input("Press Enter to Exit.")
