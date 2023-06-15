def palindrome_permutation(permutation):
    if(len(permutation) == 0):
        return False
    permutation = permutation.replace(" ", "").lower()
    countOdd = 0
    for i in permutation:
        if (permutation.count(i) % 2 == 1):
            countOdd += 1
    if countOdd > 1:
        return False
    return True


print(palindrome_permutation("aab b1"))
