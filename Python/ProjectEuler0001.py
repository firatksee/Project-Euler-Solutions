
#projecteuler.net/problem=1

#Answer: 233168

#github.com/firatksee


def multiples():
	result = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
	return result

if __name__ == "__main__":
	print(multiples())
