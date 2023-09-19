
# projecteuler.net/problem=6

# Answer: 25164150

# github.com/firatksee


def sumSqrDiff(start, stop):
    sumOfSqr = sum(map(lambda x: x**2, range(start, stop)))
    sqrOfSum = sum(range(start, stop)) ** 2

    return abs(sumOfSqr - sqrOfSum)


if __name__ == "__main__":
    print(sumSqrDiff(1, 101))
