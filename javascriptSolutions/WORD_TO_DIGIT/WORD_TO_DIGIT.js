/* https://www.codeeval.com/open_challenges/104/
WORD TO DIGIT
CHALLENGE DESCRIPTION:

Having a string representation of a set of numbers you need to print this numbers.

All numbers are separated by semicolon. There are up to 20 numbers in one line. The numbers are "zero" to "nine"

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. E.g.

zero;two;five;seven;eight;four
three;seven;eight;nine;two
OUTPUT SAMPLE:

Print numbers in the following way:

025784
37892
*/
var numberKey = {
  zero: 0,
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9
};

var wordToDigit = function(wordList) {
  var numWord = '';

  for (var i = 0; i < wordList.length; i++) {
    numWord += numberKey[wordList[i]];
  }

  return numWord;
};

var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {
  if (line !== '') {
    console.log(wordToDigit(line.split(';')));
  }
});
