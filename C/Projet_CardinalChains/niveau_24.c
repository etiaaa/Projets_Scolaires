#include <stdio.h>
#include <stdlib.h>

int niveau24 (){

    char tableau_niveau_24[4][5] = {{ 1,   1,  'x',  1  },
                                    { 1,   1,  '.',  1  },
                                    { 1,   1,   1,  'x' },
                                    { 2,  '.',  2,  'x' },
                                    { 2,   2,   1,   1  }};

    printf(tableau_niveau_24);
    return 0;
}
