#include <stdio.h>
#include <stdlib.h>

int niveau17 (){

    char tableau_niveau_17[5][5] = {{ 2,   2,   2,   1,  '.'},
                                    { 2,   2,   2,   1,   1 },
                                    { 2,   2,   1,   3,   1 },
                                    {'x',  3,   1,   1,  'x'},
                                    { 1,   1,   3,  'x', '.'}};

    printf(tableau_niveau_17);
    return 0;
}
