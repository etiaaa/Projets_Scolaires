#include <stdio.h>
#include <stdlib.h>

int niveau4 (){

    int tableau_niveau_4[4][4] = {{ 'x', 1, 1, 2},
                                  {  2,  2, 2, 2},
                                  {  1,  2, 2, 4},
                                  { 'x', 5, 5, 4}};

    printf(tableau_niveau_4);
    return 0;
}

