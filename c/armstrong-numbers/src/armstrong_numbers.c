#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    int length = snprintf(NULL, 0, "%d", candidate);
    char *s_candidate = malloc(length + 1);
    snprintf(s_candidate, length + 1, "%d", candidate);
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        int num = s_candidate[i] - '0';
        sum += pow(num, length);
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
