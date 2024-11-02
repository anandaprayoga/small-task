def findPrime(num):
    temps = []
    primes = [2]

    for i in range(1, num+1):
        if i % 2 != 0:
            for j in range(1, i):
                if i % j == 0:
                    temps.append(i)
            if len(temps) <= 1:
                if i in temps:
                    primes.append(i)
            temps = []

    return primes

def findFactor(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def findPrimeFactors(num):
    primes = findPrime(num)
    factors = findFactor(num)
    
    primeFactors = []

    for i in range(num+1):
        if i in primes and i in factors:
            primeFactors.append(i)

    return primeFactors

print(findPrimeFactors(100))