def allPrimesUpTo(num):
    primesFound = []
    for factor in range(2, num):
        for i in primesFound:
            if factor % i == 0:
                break
        else:
            primesFound.append(factor)
    return primesFound
