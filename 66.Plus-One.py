

def plusOne(digits):
    total = ""
    for digit in digits:
        total += str(digit)

    total = int(total) + 1
    result = []
    for digit in str(total):
        result.append(int(digit))

    return(result) 



print(plusOne([1,2,3]))

print(plusOne([4,3,2,1]))
