#include <stdio.h>
#include <stdlib.h>

int main() {
    char *my_strings[] = {
        "Todos Outline",
        "Process emails",
        "Review project schedule",
        "Review orders",
        "Go over sales numbers",
        "Prepare for meeting with colleagues"};
    
    // printf("%s\n\n", my_strings[0]);
    
    for (size_t i = 0; i < 6; i++) {
        char * current_string = my_strings[i];
        char * new_string;
        if (i != 0) {
            size_t len_current_string = snprintf(NULL, 0, "%s", current_string);
            size_t len_index = snprintf(NULL, 0, "%lldd", i);
            size_t needed_length = len_current_string + len_index + 2;
            new_string = malloc(needed_length * sizeof(char));
            snprintf(new_string, needed_length, "%lld%s%s", i, ". ", current_string);
        } else {
            new_string = my_strings[i]; 
        }
        size_t j = 0;
        while(new_string[j] != '\0') {
            printf("%c", new_string[j]);
            j++;
        }
        if (i == 0) {
            printf("\n\n");
        } else {
            printf("\n");
        }
    }
}