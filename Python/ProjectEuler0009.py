
# projecteuler.net/problem=9

# Answer: 31875000

# github.com/firatksee


def pythaTriplet(perimeter):
    for a in range(1, int(perimeter/3)):
        for b in range(a + 1, int(perimeter/2)):
            c = perimeter - (a + b)
            if a**2 + b**2 == c**2:
                return a * b * c

# since a < b < c,
# a cannot be bigger than 1/3 of the perimeter,
# b cannot be bigger than 1/2 of the perimeter


if __name__ == "__main__":
    print(pythaTriplet(1000))
