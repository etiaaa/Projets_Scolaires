#include <stdio.h>
#include <stdlib.h>

int niveau20 (){

    char tableau_niveau_20[7][7] = {{ 1,     2,     1,    'x',     3,     4 },
                                    { 1,     1,     1,     3,      2,    'x'},
                                    { 2,     2,     2,     1,      1,     1 },
                                    { 2,     3,     2,     1,      1,    'x'},
                                    {'x',    3,     3,     3,     'x',    4 },
                                    { 1,     1,     2,     2,      3,     3 }};

    printf(tableau_niveau_20);
    return 0;
}
