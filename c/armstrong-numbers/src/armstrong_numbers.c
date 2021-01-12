// #include <stdio.h>
// #include <stdlib.h>
#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    // get the number of digits in candidate
    int length = 0;
    int remaining = candidate;
    while (remaining > 0)
    {
        remaining = remaining / 10;
        length += 1;
    }

    // calculate the sum of the power of the digits
    int sum = 0;
    remaining = candidate;
    while (remaining > 0)
    {
        int digit = remaining % 10;
        remaining = remaining / 10;
        sum += pow2(digit, length);
    }

    return sum == candidate;
}

int pow2(int n, int m)
{
    int product = 1;
    for (int i = 0; i < m; i++)
    {
        product *= n;
    }
    return product;
}
