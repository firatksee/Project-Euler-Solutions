// projecteuler.net/problem=7

// Answer: 104743

// github.com/firatksee

function isPrime(number) {
    if (number < 2) return false;
    if (number === 2) return true;
    if (number % 2 === 0) return false;

    const limit = Math.floor(Math.sqrt(number));

    for (let i = 3; i <= limit; i += 2) {
        if (number % i === 0) return false;
    }
    return true;
}

function nthPrime(n) {
    let count = 0;
    let number = 0;
    while (count < n) {
        if (isPrime(++number)) count++;
    }
    return number;
}

console.log(nthPrime(10001));
