
# projecteuler.net/problem=10

# Answer: 142913828922

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


def sumPrimesBelow(n):
    if n <= 2:
        return 0
    result = sum(i for i in range(3, n, 2) if isPrime(i))
    return result + 2


if __name__ == "__main__":
    print(sumPrimesBelow(4))
