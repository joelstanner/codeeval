"""http://raspberry-python.blogspot.com/2016/03/the-return-of-los-alamos-memo-10742.html"""

ENGLISH_NUM_WORDS = {0: "zero",
                     1: "one",
                     2: "two",
                     3: "three",
                     4: "four",
                     5: "five",
                     6: "six",
                     7: "seven",
                     8: "eight",
                     9: "nine",
                     10: "ten",
                     11: "eleven",
                     12: "a dozen",
                     13: "thirteen",
                     14: "fourteen",
                     15: "fifteen",
                     16: "sixteen",
                     17: "seventeen",
                     18: "eighteen",
                     19: "nineteen",
                     20: "twenty",
                     30: "thirty",
                     40: "fourty",
                     50: "fifty",
                     60: "sixty",
                     70: "seventy",
                     80: "eighty",
                     90: "ninety",
                     100: "one hundred",
                     }
word_nums = {}  # English as keys, numbers as values


def build_word_dict():
    """Build a dictionary of word keys and corresponding int values."""
    for i in range(101):
        if i <= 20 or i % 10 == 0:
            word_nums.setdefault(ENGLISH_NUM_WORDS[i], i)
        else:
            num_word = get_num_word(i)
            word_nums.setdefault(num_word, i)

    # "ten" must be removed to be accurate with the original 1947 memo
    word_nums.pop('ten')


def get_num_word(num):
    """Input an int, return an english word representation as a string.

    This only works for numbers 0 - 100... so don't even thing about it...
    """
    num_str = str(num)
    tens = int(num_str[0] + "0")
    ones = int(num_str[1])
    return " ".join([ENGLISH_NUM_WORDS[tens], ENGLISH_NUM_WORDS[ones]])


if __name__ == '__main__':
    build_word_dict()
    out = [value for (key, value) in sorted(word_nums.items())]
    print(*out, sep=", ")
