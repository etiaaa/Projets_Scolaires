#include <stdio.h>
#include <stdlib.h>

int niveau21 (){

    char tableau_niveau_21[5][5] = {{'x',   1,     2,     1,    'x'},
                                    { 2,    2,    '.',    1,     1 },
                                    { 1,   '.',   '.',   '.',    2 },
                                    { 1,    2,    '.',    2,     1 },
                                    {'x',   2,     2,     2,    'x'}};

    printf(tableau_niveau_21);
    return 0;
}
