##FIND THE LONGEST SUBSTRING WITH ALPHABETICAL ORDER
##USES INBUILT DEBUGGING METHODS TO SHOW THE FUNCTION


s = "azcbobobegghaklabcdefghi"
start = 0
end = 0
temp_start = 0

for i in range(1, len(s)):
    if s[i-1] > s[i]:
        temp_start = i
        print "Value of temp start is : ",temp_start
        
    if i - temp_start > end - start:
        start = temp_start
        print "start is: ",start
        end = i
        print "end is: ",end

string = s[start:end+1]                            
print 'Longest substring in alphabetical order is:', string
print 'Length of longest substring is: ', len(string)

