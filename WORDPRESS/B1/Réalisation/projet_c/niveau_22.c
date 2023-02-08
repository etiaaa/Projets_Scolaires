#include <stdio.h>
#include <stdlib.h>

int niveau22 (){

    char tableau_niveau_22[7][5] = {{ 2,   2,     2,     2,    2,   4,  3 },
                                    { 2,  'x',    2,     4,    3,  'x', 3 },
                                    { 2,   4,     3,     2,    2,   1,  2 },
                                    { 2,  'x',    1,     2,    1,  'x', 4 },
                                    { 1,   1,     1,     2,    3,   3,  3 }};

    printf(tableau_niveau_22);
    return 0;
}

