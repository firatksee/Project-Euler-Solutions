
#projecteuler.net/problem=4

#Answer: 906609

#github.com/firatksee


def largestPalindrome(start, stop):
	result = (m*n for m in range(start, stop)
			for n in range(start, stop)
			if str(m*n) == str(m*n)[::-1])
	return result

if __name__ == "__main__":
	print(max(largestPalindrome(100, 1000)))
