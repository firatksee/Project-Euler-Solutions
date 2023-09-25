
# projecteuler.net/problem=4

# Answer: 906609

# github.com/firatksee


def largestPalindrome(start, stop):
    largest = 0
    for m in range(start, stop):
        for n in range(start, stop):
            prod = m * n
            if str(prod) == str(prod)[::-1] and prod > largest:
                largest = prod
    return largest


if __name__ == "__main__":
    print(largestPalindrome(100, 1000))
