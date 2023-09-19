
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
    result = sum(i for i in range(n) if isPrime(i))
    return result


if __name__ == "__main__":
    print(sumPrimesBelow(2000000))
