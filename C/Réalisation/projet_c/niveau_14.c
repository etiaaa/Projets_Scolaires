#include <stdio.h>
#include <stdlib.h>

int niveau14 (){

    char tableau_niveau_14[6][6] = {{'.', '.', '.', '.',  'x', '.'},
                                    { 1,   1,   1,   1,    1,  '.'},
                                    { 1,   1,   1,   1,    8,   9 },
                                    { 1,   1,  '.', '.',  '.', '.'},
                                    { 1,   1,   1,   1,    1,  '.'},
                                    { 1,   1,   1,   1,   'x', '.'}};

    printf(tableau_niveau_14);
    return 0;
}
