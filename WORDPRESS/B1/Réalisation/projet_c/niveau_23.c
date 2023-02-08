#include <stdio.h>
#include <stdlib.h>

int niveau23 (){

    char tableau_niveau_23[6][6] = {{ 2,   2,   1,   1,    4,   4 },
                                    { 2,   3,   1,   1,    1,   3 },
                                    { 2,   4,  'x', 'x',   1,   3 },
                                    { 2,   3,   4,  'x',  'x',  1 },
                                    { 3,   3,   1,   1,    3,   3 },
                                    { 3,   3,   1,   2,    2,   4 }};

    printf(tableau_niveau_23);
    return 0;
}
