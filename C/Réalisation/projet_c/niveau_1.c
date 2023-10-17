#include <stdio.h>
#include <stdlib.h>


char tableau_niveau_1[3] = {'x', '1', '1'};
char printGrille1(tableau_niveau_1){
    for ( int i = 0; i < sizeof(tableau_niveau_1); i++) {
    printf("%d \t", tableau_niveau_1[i]);
    }
    printf("\n");
    return 0;
    }
