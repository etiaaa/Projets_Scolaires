#include <stdio.h>
#include <stdlib.h>

int niveau30 (){

    char tableau_niveau_30[7][6] = {{ 3,   4,   4,   'x',   1,    2,   3 },
                                    {'x', '.',  3,    3,    4,   '.',  3 },
                                    { 3,   3,   3,   '.',   3,    3,   3 },
                                    {'x', '.',  3,    3,    3,   '.',  4 },
                                    {'x',  3,   3,    5,    3,    3,   3 }};

    printf(tableau_niveau_30);
    return 0;
}

