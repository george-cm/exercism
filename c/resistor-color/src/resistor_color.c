// #include <stdlib.h>
#include "resistor_color.h"

int color_code(resistor_band_t color)
{
    return color;
}

resistor_band_t *colors(void)
{
    static resistor_band_t all_colors[COUNT];
    for (resistor_band_t i = 0; i < COUNT; ++i)
        all_colors[i] = i;
    return all_colors;
}
