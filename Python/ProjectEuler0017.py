
#projecteuler.net/problem=17

#Answer: 21124

#github.com/firatksee


#level parameter is for telling the function if it is on the first call or not
def inWords(number, level = True):
	if level and number == 0: return "zero"

	word = ""

	if number < 20:
		word += oneToTwenty[number]
	elif 20 <= number < 100:
		word += tens[number//10] + inWords(number%10, False)
	elif 100 <= number < 1000:
		word += inWords(number//100, False) + "hundred" + ("and" if number % 100 != 0 else "") + inWords(number%100, False)
	elif 1000 <= number < 1000000:
		word += inWords(number//1000, False) + "thousand" + inWords(number%1000, False)

	return word


oneToTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
	       "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty","ninety"]


def letterCount(start, stop):
	return sum(len(inWords(n)) for n in range(start, stop))


if __name__ == "__main__":
	print(letterCount(1,1001))
