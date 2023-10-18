#include <stdio.h>
#include <stdlib.h>

int niveau28 (){

    char tableau_niveau_28[5][5] = {{ 2,  '.',  1,   1,   1 },
                                    { 2,   2,   1,   1,   1 },
                                    { 1,   1,   1,   1,   1 },
                                    { 1,   1,   1,   1,   1 },
                                    {'.',  1,  'x',  1,   1 }};

    printf(tableau_niveau_28);
    return 0;
}

