
#projecteuler.net/problem=4

#Answer: 906609

#github.com/firatksee


def largestPalindrome():
	result = (m*n for m in range(100,1000)
			for n in range(100,1000)
			if str(m*n) == str(m*n)[::-1])
	return result

if __name__ == "__main__":
	print(max(largestPalindrome()))
