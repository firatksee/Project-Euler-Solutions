
# projecteuler.net/problem=3

# Answer: 6857

# github.com/firatksee


def primeFactorsOf(number):
    primeFactors, divisor = set(), 2

    while number > 1:
        if number % divisor == 0:
            primeFactors.add(divisor)
            number /= divisor
        else:
            divisor += 1
    return primeFactors


if __name__ == "__main__":
    print(max(primeFactorsOf(600851475143)))
