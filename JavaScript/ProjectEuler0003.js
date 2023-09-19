// projecteuler.net/problem=3

// Answer: 6857

// github.com/firatksee

function primeFactorsOf(number) {
    const primeFactors = new Set();
    let divisor = 2;

    while (number > 1) {
        if (number % divisor === 0) {
            primeFactors.add(divisor);
            number /= divisor;
        } else {
            divisor++;
        }
    }

    return Array.from(primeFactors);
}

const maxPrimeFactor = Math.max(...primeFactorsOf(600851475143));

console.log(maxPrimeFactor);
