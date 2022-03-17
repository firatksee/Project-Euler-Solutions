
#projecteuler.net/problem=14

#Answer: 837799

#github.com/firatksee


collatzMemory = {1:1}

def lenCollatz(n):
	if n in collatzMemory: return collatzMemory[n]

	nextNum = int(n/2) if n % 2 == 0 else n*3 + 1
	result = lenCollatz(nextNum) + 1

	collatzMemory[n] = result
	return result


def longestCollatzBelow(n):
	for i in range(1, n):
		lenCollatz(i)

	longestChain = max(collatzMemory.values())

	for key, value in collatzMemory.items():
		if value == longestChain:
			return key


if __name__ == "__main__":
	print(longestCollatzBelow(1000000))
