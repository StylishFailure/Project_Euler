i = 1
upperLimit = 1000
firstNumber = 3 
secondNumber = 5
total = 0

while i < upperLimit:
    if i % firstNumber == 0:
        total += i
        i += 1
    elif i % secondNumber == 0: 
        total += i
        i+=1
    else: 
        i += 1

print("The sum of all of the multiples of " + str(firstNumber) + " and " + str(secondNumber) + " below " + str(upperLimit) + " is " + str(total) + ".")