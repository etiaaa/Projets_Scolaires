#include <stdio.h>
#include <stdlib.h>

int niveau5 (){

    char tableau_niveau_5[4][5] = {{ 'x', 1,  2,  3 },
                                   {  5,  4, 'x', 3 },
                                   {  5,  4,  6,  6 },
                                   {  7,  6,  2,  2 },
                                   {  8,  5,  4, 'x'}};

    printf(tableau_niveau_5);
    return 0;
}
