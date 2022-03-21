
#projecteuler.net/problem=16

#Answer: 1366

#github.com/firatksee


def powerDigitSum(n):
	result = sum(int(i) for i in str(2**n))
	return result

if __name__ == "__main__":
	print(powerDigitSum(1000))
