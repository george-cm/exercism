#include <stdlib.h>
#include "isogram.h"

bool is_isogram(const char phrase[])
{
    if (phrase == NULL)
    {
        return false;
    }

    int i = 0;
    int j = 1;
    while (phrase[i] != '\0')
    {
        if (phrase[i] != '-' && phrase[i] != ' ')
        {
            while (phrase[j] != '\0')
            {
                if (phrase[j] != '-' && phrase[j] != ' ')
                {
                    if (lower(phrase[i]) == lower(phrase[j]))
                    {
                        return false;
                    }
                }
                j += 1;
            }
        }
        i += 1;
        j = i + 1;
    }
    return true;
}

char lower(char c)
{
    if (c >= 'A' && c <= 'Z')
    {
        return c - 'A' + 'a';
    }
    return c;
}