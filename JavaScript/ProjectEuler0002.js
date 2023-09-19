// projecteuler.net/problem=2

// Answer: 4613732

// github.com/firatksee

// recursive fibonacci algorithm, base cases 0 and 1 return 1
/*
function fibonacci(step) {
    return step < 2 ? 1 : fibonacci(step - 1) + fibonacci(step - 2);
}
*/

// since the following algorithm is more optimized for this solution,
// we will not use recursive fibonacci algorithm

function fibonacciSumEven(limit) {
    let result = 0;

    let prev = 1;
    let value = 1;

    while (value <= limit) {
        if (value % 2 === 0) result += value;
        const nextVal = prev + value;
        prev = value;
        value = nextVal;
    }

    return result;
}

console.log(fibonacciSumEven(4000000));
