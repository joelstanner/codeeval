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

english_list = []


def main():
    for i in range(101):
        if i <= 20:
            english_list.append(ENGLISH_NUM_WORDS[i])
        elif i < 100:
            num_word = get_num_word(i)
            english_list.append(num_word)
        else:
            english_list.append(ENGLISH_NUM_WORDS[i])

    # "ten" must be removed to be accurate with the original 1947 memo
    english_list.remove('ten')
    return sorted(english_list)


def get_num_word(num):
    num_str = str(num)
    tens = int(num_str[0] + "0")
    ones = int(num_str[1])
    return " ".join([ENGLISH_NUM_WORDS[tens], ENGLISH_NUM_WORDS[ones]])
