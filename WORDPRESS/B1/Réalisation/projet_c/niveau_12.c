#include <stdio.h>
#include <stdlib.h>

int niveau12 (){

    char tableau_niveau_12[5][5] = {{ 1,  1,   1,  3, 4},
                                    { 1, '.',  1,  3, 5},
                                    { 1, 'x',  1,  3, 3},
                                    { 1, '.',  1,  1, 3},
                                    { 1,  1,   1,  2, 2}};

    printf(tableau_niveau_12);
    return 0;
}
