#include <stdio.h>
#include <stdlib.h>

int niveau27 (){

    char tableau_niveau_27[7][6] = {{ 1,   4,   4,   '.',   3,    3,   4 },
                                    { 1,   3,   3,    3,    3,    3,   1 },
                                    { 1,   4,   4,    4,   'x',   2,  'x'},
                                    {'x', 'x',  4,    4,    1,    2,   3 },
                                    { 6,   6,   5,    5,    6,   'x',  1 },
                                    { 5,   5,   5,   '.',   6,    6,   6 }};

    printf(tableau_niveau_27);
    return 0;
}

