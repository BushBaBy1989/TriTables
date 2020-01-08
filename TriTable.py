#Decalare variable to be used for printing
multiplyString = ""

#Next for loops to loop through the numbers we wish to multiply
#Outer loop controls the number being multiplies and Inner loop controls how many times you want to multiply it
for x in range (1, 10):
    for y in range (1, x+1):
        multiplyString = multiplyString + str(x * y) + "\t"
    print(multiplyString)
    multiplyString = ""
