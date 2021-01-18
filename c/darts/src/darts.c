#include <math.h>
#include "darts.h"

int score(coordinate_t pos)
{
    const int inner_r = 1;
    const int middle_r = 5;
    const int outer_r = 10;

    if (sqrt(pos.x * pos.x + pos.y * pos.y) > outer_r)
    {
        return 0;
    }

    if (sqrt(pos.x * pos.x + pos.y * pos.y) > middle_r)
    {
        return 1;
    }

    if (sqrt(pos.x * pos.x + pos.y * pos.y) > inner_r)
    {
        return 5;
    }

    return 10;
}