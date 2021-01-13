#include <stdlib.h>
#include "resistor_color.h"

int color_code(resistor_band_t color)
{
    // switch (color)
    // {
    // case BLACK:
    //     return 0;
    //     break;
    // case BROWN:
    //     return 1;
    //     break;
    // case RED:
    //     return 2;
    //     break;
    // case ORANGE:
    //     return 3;
    //     break;
    // case YELLOW:
    //     return 4;
    //     break;
    // case GREEN:
    //     return 5;
    //     break;
    // case BLUE:
    //     return 6;
    //     break;
    // case VIOLET:
    //     return 7;
    //     break;
    // case GREY:
    //     return 8;
    //     break;
    // case WHITE:
    //     return 9;
    //     break;

    // default:
    //     return -1;
    //     break;
    // }
    return color;
}

resistor_band_t *colors(void)
{
    resistor_band_t *all_colors = malloc(10 * sizeof(resistor_band_t));
    all_colors[0] = BLACK;
    all_colors[1] = BROWN;
    all_colors[2] = RED;
    all_colors[3] = ORANGE;
    all_colors[4] = YELLOW;
    all_colors[5] = GREEN;
    all_colors[6] = BLUE;
    all_colors[7] = VIOLET;
    all_colors[8] = GREY;
    all_colors[9] = WHITE;

    return all_colors;
}
