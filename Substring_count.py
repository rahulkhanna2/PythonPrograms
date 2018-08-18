x = "bobisabadguybobisacrookbelikebob"

count = 0
sub = "bob"

for i in range(len(x)):
        if x[i:i+ len(sub)] == sub:
             count = count +1

print count
        
