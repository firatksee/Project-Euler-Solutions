
# projecteuler.net/problem=2

# Answer: 4613732

# github.com/firatksee


# recursive fibonacci algorithm, base cases 0 and 1 return 1
"""
def fibonacci(step):
	return 1 if step < 2 else fibonacci(step - 1) + fibonacci(step - 2)
"""

# since the following algorithm is more optimized for this solution,
# we will not use recursive fibonacci algorithm


def fibonacciSumEven(limit):
    result, prevValue, value = 0, 1, 1

    while value <= limit:
        result += value if value % 2 == 0 else 0
        prevValue, value = value, prevValue + value

    return result


if __name__ == "__main__":
    print(fibonacciSumEven(4000000))
