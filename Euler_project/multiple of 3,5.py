def smulti(n):
    total = 0
    for i in range(1, n):
        if (i % 3 == 0 or i % 5 == 0):
            total += i
    return total


print(smulti(1000))
