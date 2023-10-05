// projecteuler.net/problem=9

// Answer: 31875000

// github.com/firatksee

function pythaTriplet(perimeter) {
    for (let a = 0; a < perimeter / 3; a++) {
        for (let b = a + 1; b < perimeter / 2; b++) {
            let c = perimeter - (a + b);
            if (a * a + b * b === c * c) {
                return a * b * c;
            }
        }
    }
}

// since a < b < c,
// a cannot be bigger than 1/3 of the perimeter,
// b cannot be bigger than 1/2 of the perimeter

console.log(pythaTriplet(1000));
