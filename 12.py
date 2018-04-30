def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


primes = []
x = 10001
n = 2

while len(primes) != x+1:
    if is_prime(n):
        primes.append(n)
    n += 1


print(primes[-1])
