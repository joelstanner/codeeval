/* Write a program which finds the next-to-last word in a string.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input
example is the following:

some line with text
another line

Each line has more than one word.

OUTPUT SAMPLE:

Print the next-to-last word in the following way:

with
another
*/

function penultimate(line) {
    var words = line.split(" ")
    console.log(words[words.length - 2])
}


var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString()
                                .split('\n')
                                .forEach(function (line) {
    if (line !== "") {
        penultimate(line)
    }
});