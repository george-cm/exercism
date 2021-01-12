#include <stdio.h>
#include <stdlib.h>
#include "armstrong_numbers.h"

bool is_armstrong_number1(int candidate)
{
    int length = snprintf(NULL, 0, "%d", candidate);
    char *s_candidate = malloc(length + 1);
    snprintf(s_candidate, length + 1, "%d", candidate);
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        int num = s_candidate[i] - '0';
        sum += pow2(num, length);
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

bool is_armstrong_number2(int candidate)
{
    int digit;
    int remaining;
    int sum = 0;
    int *digits = malloc(sizeof(int));
    int length = 0;

    remaining = candidate;
    while (remaining > 0)
    {
        digit = remaining % 10;
        remaining = remaining / 10;
        length += 1;
        digits = realloc(digits, length * sizeof(int));
        *(digits + length - 1) = digit;
    }

    for (int i = 0; i < length; i++)
    {
        sum += pow2(*(digits + i), length);
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
