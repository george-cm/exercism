#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

typedef enum
{
    BLACK,
    BROWN,
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    VIOLET,
    GREY,
    WHITE,
    COUNT
} resistor_band_t;

#endif

int color_code(resistor_band_t color);
resistor_band_t *colors(void);
