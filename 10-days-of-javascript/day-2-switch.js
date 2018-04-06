'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letterArray = {
        'A': ['a', 'e', 'i', 'o', 'u'],
        'B': ['b', 'c', 'd', 'f', 'g'],
        'C': ['h', 'j', 'k', 'l', 'm'],
        'D': ['n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'],
    };

    for (let letter in letterArray) {
        if (letterArray[letter].includes(s.charAt(0))) {
            return letter;
        }
    }
    return false;
}

function main() {
    const s = readLine();

    console.log(getLetter(s));
}