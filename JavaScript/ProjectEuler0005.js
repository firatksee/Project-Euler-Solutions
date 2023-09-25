// projecteuler.net/problem=5

// Answer: 232792560

// github.com/firatksee

// least-common-divisor algorithm; explained in the end of the file
function lcm(a, b) {
    const max = Math.max(a, b);
    const min = Math.min(a, b);

    for (let i = max; i <= a * b; i += max) {
        if (i % min === 0) return i;
    }
}

function smallestMultiple(start, stop) {
    result = 1;
    for (let i = start; i < stop; i++) {
        result = lcm(result, i);
    }
    return result;
}

console.log(smallestMultiple(1, 21));

// lcm algorithm explanation:
/*
result must be between the biggest number and the multiple of all the numbers,
and since it must be a multiple of the biggest number, algorithm iterates
this interval with a step of the bigger number,
the first (smallest) number to be divided by the other number with remainder 0
is the result
*/
