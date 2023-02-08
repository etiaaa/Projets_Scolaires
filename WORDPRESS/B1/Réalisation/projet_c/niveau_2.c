#include <stdio.h>
#include <stdlib.h>


char tableau_niveau_2[3][3] = {{'x', '1', '1' },
                               {'2', '2', '2' },
                               {'3', '3', '3' }};

char printGrille2(char tableau_niveau_2[3][3]){
    for ( int i = 0; i < sizeof(tableau_niveau_2[i]); i++) {
            for (int j = 0; j < sizeof(tableau_niveau_2[i]); j++ ) {
                printf("%c \t", tableau_niveau_2[i][j]);
            }
            printf("\n");
    }

        return 0;
}


