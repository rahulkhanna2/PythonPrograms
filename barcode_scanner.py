#BARCODE SCANNER VALUES


##file = open("testFile.txt", "w")
##
price = {"8902519010124": 55 , "9781259061080": 458 , "9788126525980":699 , "9788131716830":650}
total = 0
##
##while True:
##    y = raw_input();
##    if y == "":
##        break
##    else:
##        file.write(y + "\n");
##
####file.write("Hello World")
##
##file.close()  
##
##fRead = open("testFile.txt","r")
##for product in fRead:
##    total += price[product[:len(product)-1]]
##
##print total
##
##

while True:
    x = raw_input()
    if x!= "":
        total += price[x]
    else:
        break

print total
