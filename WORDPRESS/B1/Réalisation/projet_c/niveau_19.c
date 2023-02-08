#include <stdio.h>
#include <stdlib.h>

int niveau19 (){

    char tableau_niveau_19[7][7] = {{ 1,     1,    'x',    2,     2,     2,     1 },
                                    { 1,    '.',   '.',    2,    '.',   '.',    1 },
                                    { 1,    '.',   'x',    2,     2,    '.',    1 },
                                    { 1,     2,     1,    'x',    1,    'x',    1 },
                                    { 2,    '.',    1,     1,     2,    '.',    2 },
                                    { 2,    '.',   '.',    1,    '.',   '.',    2 },
                                    { 2,     2,     1,     1,    'x',    1,     2 }};

    printf(tableau_niveau_19);
    return 0;
}
