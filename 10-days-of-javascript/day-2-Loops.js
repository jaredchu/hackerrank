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

function vowelsAndConsonants(s) {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let charList = s.split('');
    s.split('').forEach(function (char) {
        if (vowels.includes(char)) {
            console.log(char);
            charList.splice(charList.indexOf(char), 1)
        }
    });

    charList.forEach(function (char) {
        console.log(char);
    })
}

function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}