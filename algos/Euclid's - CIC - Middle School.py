import math

def Euclids(n, m):
    while n != 0:
        r = m%n
        m = n
        n = r
    return m

###################################

def CIC(m,n):
    t = min(m,n)
    for i in range (t, 1, -1):
        if (m%i == 0):
            if (n%i == 0):
                return i

###################################

def SieveofEratosthenos(n):
    primes = []
    for i in range (2,n + 1):
        primes.append(i)
    for i in range (2, math.floor(math.sqrt(n)) + 1):
        if i in primes:
            for j in range (i*i, n+1, i):
                if j in primes:
                    primes.remove(j)

    return primes

def primeFactorization(n):
    primes = SieveofEratosthenos(n)

    factors = []
    
    while n != 1:
        for i in primes:
            while n % i == 0:
                n /= i
                factors.append(i)
    return factors

def MiddleSchoolProcedure(m,n):
    factorsM = primeFactorization(m)
    factorsN = primeFactorization(n)
    
    print (factorsM, "\n",factorsN)
    
    commonFactors = []

    for num in factorsM:
        if num in factorsN:
            commonFactors.append(num)
            factorsN.remove(num)

    print(commonFactors)
    gcd = 1;
    for i in commonFactors:
        gcd *= i
    print (gcd)
    return gcd
    
