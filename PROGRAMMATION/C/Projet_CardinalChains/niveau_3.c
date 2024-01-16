#include <stdio.h>
#include <stdlib.h>



char tableau_niveau_3[3][4] = {{ 'x', '1',  '1',  '2'},
                               { '3', '2',  '2',  '1'},
                               { '3', '3',  '3',  'x'}};

char printGrille3(char tableau_niveau_3[3][4]){
    for (int i = 0; i < sizeof(tableau_niveau_3[i]); i++) {
            for (int j = 0; j < sizeof(tableau_niveau_3[i]); j++ ) {
                printf("%c \t", tableau_niveau_3[i][j]);

            }
            printf("\n");
    }

        return 0;
}

