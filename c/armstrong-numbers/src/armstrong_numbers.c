#include <stdio.h>
#include <stdlib.h>
#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    int digit;
    int remaining;
    int sum = 0;
    int length = 0;

    remaining = candidate;
    while (remaining > 0)
    {
        digit = remaining % 10;
        remaining = remaining / 10;
        length += 1;
    }

    remaining = candidate;
    while (remaining > 0)
    {
        digit = remaining % 10;
        remaining = remaining / 10;
        sum += pow2(digit, length);
    }

    if (sum == candidate)
    {
        return true;
    }
    else
    {
        return false;
    }
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
