/*https://www.codeeval.com/open_challenges/103/
LOWEST UNIQUE NUMBER
CHALLENGE DESCRIPTION:

There is a game where each player picks a number from 1 to 9, writes it on a
paper and gives to a guide. A player wins if his number is the lowest unique.
We may have 10-20 players in our game.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.

You're a guide and you're given a set of numbers from players for the round of
game. E.g. 2 rounds of the game look this way:

3 3 9 1 6 5 8 1 5 3
9 2 9 9 1 8 8 8 2 1 1
OUTPUT SAMPLE:

Print a winner's position or 0 in case there is no winner. In the first line of
input sample the lowest unique number is 6. So player 5 wins.

5
0
*/
var onlyUnique = function(value, index, self) {
    return self.indexOf(value) === index;
};

var findLowest = function (numbers) {
    // clone and sort original array
    var clone = numbers.slice().sort(),
        unique = clone.filter(onlyUnique),
        idx,
        i;

    // find the lowest
    for (i = 0; i < unique.length; i++) {
        idx = clone.indexOf(unique[i]);
        if (clone[idx + 1] !== unique[i]) {
            // return seat position, which starts at 1 index
            return numbers.indexOf(unique[i]) + 1;
        }
    }
    return 0;
    // return lowest or 0 if there is none
};


var fs  = require("fs"),
    result = 0;

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        result = findLowest(line.split(' ').map(Number));
        console.log(result);
    }
});
