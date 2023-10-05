// projecteuler.net/problem=10

// Answer: 142913828922

// github.com/firatksee

function isPrime(number) {
    if (number < 2) return false;
    if (number === 2) return true;
    if (number % 2 === 0) return false;

    for (let i = 3; i <= Math.sqrt(number); i += 2) {
        if (number % i === 0) return false;
    }
    return true;
}

function sumPrimesBelow(n) {
    let result = 2;

    for (let i = 3; i < n; i += 2) {
        if (isPrime(i)) result += i;
    }

    return result;
}

console.log(sumPrimesBelow(2000000));
