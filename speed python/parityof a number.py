def checkevenodd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


print(checkevenodd(15))


def checkParity(n):
    result = (n % 2)
    return result


print("Odd parity", checkParity(17))
print("Even parity", checkParity(16))