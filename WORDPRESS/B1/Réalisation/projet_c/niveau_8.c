#include <stdio.h>
#include <stdlib.h>

int niveau8(){

    char tableau_niveau_8[4][4] = {{ 'x', 5,  6,  8},
                                   {  3,  4,  7,  8},
                                   {  4,  3, 'x', 1},
                                   { 'x', 3,  5,  3}};

    printf(tableau_niveau_8);
    return 0;
}

