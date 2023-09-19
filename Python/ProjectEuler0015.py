
# projecteuler.net/problem=15

# Answer: 137846528820

# github.com/firatksee


# to reach from a corner to across of a grid m x n, there are two indistinguishable directions,
# that are m and n long. so the problem requires a permutation solution with 2 indistinguishable values

def latticePaths(m, n):
    return factorial(m + n) // (factorial(m) * factorial(n))


def factorial(n):
    assert n >= 0
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(latticePaths(20, 20))
