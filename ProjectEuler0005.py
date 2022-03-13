
#projecteuler.net/problem=5

#Answer: 232792560

#github.com/firatksee


#least-common-divisor algorithm; explained in the end of the file
def lcm(a, b):
	for i in range(max(a, b), a * b + 1, max(a, b)):
		if i % min(a, b) == 0:
			return i


def smallestMultiple(start, stop):
	result = 1
	for i in range(start, stop):
		result = lcm(result, i)
	return result


if __name__ == "__main__":
	print(smallestMultiple(1,21))


#lcm algorithm explanation:
"""
result must be between the biggest number and the multiple of all the numbers,
and since it must be a multiple of the biggest number, algorithm iterates
this interval with a step of the bigger number,
the first (smallest) number to be divided by the other number with remainder 0
is the result
"""
