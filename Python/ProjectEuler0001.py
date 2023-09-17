
# projecteuler.net/problem=1

# Answer: 233168

# github.com/firatksee


def multiples(limit):
    result = sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)
    return result


if __name__ == "__main__":
    limit = 1000
    print(multiples(limit))
