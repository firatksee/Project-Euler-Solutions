// projecteuler.net/problem=1

// Answer: 233168

// github.com/firatksee

function multiples(limit) {
    let result = 0;

    for (let i = 0; i < limit; i++) {
        if (i % 3 === 0 || i % 5 === 0) result += i;
    }

    return result;
}

console.log(multiples(1000));
