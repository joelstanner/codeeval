/*
You have a set of rows with names of famous writers encoded inside. Each row is
divided into 2 parts by pipe char (|). The first part has a writer's name. The
second part is a "key" to generate a name.

Your goal is to go through each number in the key (numbers are separated by
space) left-to-right. Each number represents a position in the 1st part of a
row. This way you collect a writer's name which you have to output.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input
example is the following

osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53

3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31

This input had 2 rows.

OUTPUT SAMPLE:

Print results in the following way.

Stephen King 1947
Kyotaro Nishimura 1930
*/

var findWriter = function (line) {
    var code = line.split('|'),
        numsStr = code[1].split(' '),
        numsInt = [],
        auth = ""
    
    // skip the first array item - it's an empty string    
    for (var i=1; i < numsStr.length; i++) {
        numsInt.push(parseInt(numsStr[i], 10));
    }
    
    // cypher code is 1 based start of index
    for (i=0; i < numsInt.length; i++) {
        auth += code[0][numsInt[i] - 1]
    }
    return auth;
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString()
                                .split('\n')
                                .forEach(function (line) {
    if (line !== "") {
        var result = findWriter(line)
        console.log(result)
    }
});
