/*
 Write a program which capitalizes the first letter of each word in a sentence.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
Input example is the following

Hello world
javaScript language
a letter
1st thing

OUTPUT SAMPLE:

Print capitalized words in the following way.

Hello World
JavaScript Language
A Letter
1st Thing
*/

String.prototype.ucfirst = function() {
    return this.charAt(0).toUpperCase() + this.substr(1);
}


function capWords(line) {
    var words = line.split(" "),
        upperWords = [];
    for (var i=0; i < words.length; i++) {
        upperWords.push(words[i].ucfirst());
    }
    return upperWords.join(" ");
}


var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString()
                                .split('\n')
                                .forEach(function (line) {
    if (line !== "") {
        var result = capWords(line)
        console.log(result)
    }
});
