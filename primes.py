def findPrime(num):
    temp = []
    prime = [2]

    for i in range(1, num+1):
        if i % 2 != 0:
            for j in range(1, i):
                if i % j == 0:
                    temp.append(i)
            if len(temp) <= 1:
                if i in temp:
                    prime.append(i)
            temp = []

    return prime

findPrime(50)