
# projecteuler.net/problem=12

# Answer: 76576500

# github.com/firatksee


def triangleNum(nth):
    # "sum(i for i in range(1, nth + 1))" using this algorithm (brute force) instead,
    return int(nth*(nth + 1)/2)
    # would double the time for considerably large inputs


def factorNumOf(n):    # more readable code for this algorithm is available in the end of the file
    n_sqrt = n**0.5
    return sum(1 for i in range(1, int(n_sqrt) + 1) if n % i == 0) * 2 - (1 if n_sqrt == int(n_sqrt) else 0)


def divisibleTriNum(factorNum):
    step = 1
    while True:
        triangularNum = triangleNum(step)
        if factorNumOf(triangularNum) > factorNum:
            return triangularNum
        step += 1


if __name__ == "__main__":
    print(divisibleTriNum(500))


# more readable code for the function factorNumOf():
"""
def factorNumOf(n):
	n_sqrt = n**0.5
	result = 0
	
	for i in range(1, int(n_sqrt) + 1):
		if n % i == 0:
			result += 1
	
	result *= 2
	
	if n_sqrt == int(n_sqrt):
		result -= 1

	return result
"""
