/* https://www.codeeval.com/open_challenges/106/
ROMAN NUMERALS
CHALLENGE DESCRIPTION:

Many persons are familiar with the Roman numerals for relatively small numbers.
The symbols I (capital i), V, X, L, C, D, and M represent the decimal
values 1, 5, 10, 50, 100, 500 and 1000 respectively. To represent other
values, these symbols, and multiples where necessary, are concatenated,
with the smaller-valued symbols written further to the right. For example,
the number 3 is represented as III, and the value 73 is represented as LXXIII.
The exceptions to this rule occur for numbers having units values of 4 or 9,
and for tens values of 40 or 90. For these cases, the Roman numeral
representations are IV (4), IX (9), XL (40), and XC (90). So the Roman
numeral representations for 24, 39, 44, 49, and 94 are
XXIV, XXXIX, XLIV, XLIX, and XCIV, respectively.

Write a program to convert a cardinal number to a Roman numeral.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
Input example is the following

159
296
3992
Input numbers are in range [1, 3999]

OUTPUT SAMPLE:

Print out Roman numerals.

CLIX
CCXCVI
MMMCMXCII
*/
var romans = function(number) {
  var digits = {
        thousands: 0,
        hundreds: 0,
        tens: 0,
        ones: 0
      },
      romanStr = '';

  for (var i = 1; i < number.length; i++) {
    if (number.slice(-1) !== '') {
      digits.ones = parseInt(number.slice(-1), 10);
    }
    if (number.slice(-2, -1) !== '') {
      digits.tens = parseInt(number.slice(-2, -1), 10);
    }
    if (number.slice(-3, -2) !== '') {
      digits.hundreds = parseInt(number.slice(-3, -2), 10);
    }
    if (number.slice(-4, -3) !== '') {
      digits.thousands = parseInt(number.slice(-4, -3), 10);
    }
  }

  // Construct the roman numeral string
  // Thousands
  romanStr += Array(digits.thousands + 1).join('M');
  // Hundreds
  if (digits.hundreds < 4) {
    romanStr += Array(digits.hundreds + 1).join('C');
  } else if (digits.hundreds === 4) {
    romanStr += 'CD';
  } else if (digits.hundreds < 9) {
    romanStr += 'D' + Array(digits.hundreds - 4).join('C');
  } else {
    romanStr += 'CM';
  }
  // Tens
  if (digits.tens < 4) {
    romanStr += Array(digits.tens + 1).join('X');
  } else if (digits.tens === 4) {
    romanStr += 'XL';
  } else if (digits.tens < 9) {
    romanStr += 'L' + Array(digits.tens - 4).join('X');
  } else {
    romanStr += 'XC';
  }
  // Ones
  if (digits.ones < 4) {
    romanStr += Array(digits.ones + 1).join('I');
  } else if (digits.ones === 4) {
    romanStr += 'IV';
  } else if (digits.ones < 9) {
    romanStr += 'V' + Array(digits.ones - 4).join('I');
  } else {
    romanStr += 'IX';
  }

  return romanStr;
};

var fs = require('fs');
fs.readFileSync(process.argv[2]).toString()
                                .split('\n')
                                .forEach(function(line) {
    if (line !== '') {
      console.log(romans(line));
    }
});
