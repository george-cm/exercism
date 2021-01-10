"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        if (sum(dice)/5 == dice[0]):
            return YACHT
        else:
            return 0
    for i in range(1, 7):
        if category == i:
            return dice.count(i) * i
    if category == CHOICE:
        return sum(dice)

    counts = {}
    for num in dice:
        counts[num] = counts.get(num, 0) + 1

    if category == FULL_HOUSE:
        if len(counts.keys()) == 2:
            v1, v2 = counts.values()
            if abs(v1 - v2) == 1:
                return sum(dice)
            else:
                return 0
        else:
            return 0

    if category == FOUR_OF_A_KIND:
        for k, v in counts.items():
            if v >= 4:
                return k * 4
        return 0

    if category == LITTLE_STRAIGHT:
        i = 1
        for num in sorted(dice):
            if num == i:
                i += 1
            else:
                break
        return 30 if i == 6 else 0
    if category == BIG_STRAIGHT:
        i = 2
        for num in sorted(dice):
            if num == i:
                i += 1
            else:
                break
        return 30 if i == 7 else 0
