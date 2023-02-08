#include <stdio.h>
#include <stdlib.h>

int niveau16 (){

    char tableau_niveau_16[5][5] = {{ 4,   4,   4,   4,   4},
                                    { 4,   2,   2,   2,   4},
                                    { 4,   2,  'x',  4,   4},
                                    { 4,   2,   2,   4,   4},
                                    { 4,   4,   4,   6,   8}};

    printf(tableau_niveau_16);
    return 0;
}
