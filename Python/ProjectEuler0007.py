
# projecteuler.net/problem=7

# Answer: 104743

# github.com/firatksee


def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def nthPrime(n):
    count, number = 0, 0
    while count < n:
        number += 1
        if isPrime(number):
            count += 1
    return number


if __name__ == "__main__":
    print(nthPrime(10001))
