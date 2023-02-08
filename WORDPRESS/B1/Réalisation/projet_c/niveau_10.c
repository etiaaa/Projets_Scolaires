#include <stdio.h>
#include <stdlib.h>

int niveau10 (){

    char tableau_niveau_10[8][8] = {{ 'x', 1,  1,  4,   4,   2,   1, 'x'},
                                    {  2,  3, 'x', 5,   6,  'x',  1,  1 },
                                    {  2,  4,  9,  8,   7,   9,   2,  2 },
                                    {  4,  5,  9, 'x', 'x',  9,   2,  3 },
                                    {  5,  6,  9,  9,   4,   9,   9,  3 },
                                    {  6,  7,  9,  9,   5,   8,   8,  4 },
                                    {  7,  8,  9,  9,   5,   8,   7,  5 },
                                    {  7,  9,  9,  9,   6,   7,   6,  5 }};

    printf(tableau_niveau_10);
    return 0;
}
