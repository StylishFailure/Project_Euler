i = 1 
j = 2 
upperLimit = 4000000
fibonacci = [1]
evenFibonacci = []

while j < upperLimit: 
    fibonacci.append(j)
    j += fibonacci[i-1]
    i += 1

arrayLength = len(fibonacci)

for x in fibonacci: 
    p = fibonacci[x]
    if p > 0 and p % 2  == 0:
        break

i = fibonacci.index(p) 

while i < arrayLength:
    evenFibonacci.append(fibonacci[i])
    i +=3

print("The sum of all even-valued terms in the fibonacci sequence, whose values do not exceed four million is " + str(sum(evenFibonacci)) +" . ")