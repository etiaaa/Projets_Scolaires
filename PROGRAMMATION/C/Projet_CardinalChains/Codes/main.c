#include <stdio.h>
#include <stdlib.h>
#include "niveau_1.c"
#include "niveau_2.c"
#include "niveau_3.c"
int main(){

    printGrille1(tableau_niveau_1);
    printf("\n");

    printGrille2(tableau_niveau_2);
    printf("\n");

    printGrille3(tableau_niveau_3);
    return 0;

}
