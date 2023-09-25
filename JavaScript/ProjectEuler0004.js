// projecteuler.net/problem=4

// Answer: 906609

// github.com/firatksee

function isPalindrome(value) {
    const valueStr = value.toString();
    const revValueStr = valueStr.split("").reverse().join("");
    return valueStr === revValueStr;
}

function largestPalindrome(start, stop) {
    let largest = 0;
    for (let m = start; m < stop; m++) {
        for (let n = start; n < stop; n++) {
            let prod = m * n;
            if (isPalindrome(prod) && prod > largest) largest = prod;
        }
    }
    return largest;
}

console.log(largestPalindrome(100, 1000));
