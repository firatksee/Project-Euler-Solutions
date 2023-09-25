// projecteuler.net/problem=6

// Answer: 25164150

// github.com/firatksee

function sumSqrDiff(start, stop) {
    let sumOfSqr = 0;
    let sum = 0;

    for (let i = start; i < stop; i++) {
        sumOfSqr += i * i;
        sum += i;
    }

    const sqrOfSum = sum * sum;

    return Math.abs(sumOfSqr - sqrOfSum);
}

console.log(sumSqrDiff(1, 101));
