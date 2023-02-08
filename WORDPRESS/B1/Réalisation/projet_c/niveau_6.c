#include <stdio.h>
#include <stdlib.h>

int niveau6 (){

    char tableau_niveau_6[6][6] = {{ 'x', 3,  3,  5,  5,  5},
                                   {  1,  2,  4,  5,  6,  6},
                                   {  2,  3, 'x', 5,  5,  8},
                                   { 'x', 3,  9,  7,  8,  8},
                                   {  5,  4,  8,  6,  5,  4},
                                   {  5,  6,  7, 'x', 2,  3}};

    printf(tableau_niveau_6);
    return 0;
}
