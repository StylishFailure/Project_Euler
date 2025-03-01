firstPalindrome = 997 
i = 1 
while i < 987 : 
    j = 999 
    backPalindrome = [int(str(firstPalindrome)[2]), int(str(firstPalindrome)[1]), int(str(firstPalindrome)[0])]
    s = ''.join(str(x) for x in backPalindrome)
    finalPalindrome = (firstPalindrome*1000) + int(s)
    while j > 100: 
        if finalPalindrome  % j >= 1: 
            j -= 1 
        elif (finalPalindrome / j ) > 999: 
            j -= 1
        else: 
            break 
    if finalPalindrome % j == 0:
        print(str(finalPalindrome) + " is the largest palindrome of the product of two 3-digit numbers. It is the product of " + str(j) + " and " + str(int(finalPalindrome / j)) + ".")
        break
    else: 
        firstPalindrome -= 1 
        i +=1 