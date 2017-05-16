
#include<stdio.h>

int main()
{

    float quot, matrix[20][20];
    signed int det;
    int i, j;
    int t, n;

    printf("enter size  of the matrix\n: ");

    scanf("%d", &n);

    printf(" enter the matrix: \n");

    for(i = 0; i < n; i++){

        for(j = 0; j < n; j++){

            scanf("%f", &matrix[i][j]);

        }

    }


    for(i = 0; i < n; i++){

        for(j = 0; j < n; j++){

            if(j>i){

                quot = matrix[j][i]/matrix[i][i];

                for(t = 0; t < n; t++){

                    matrix[j][t] =matrix[j][t]-( quot * matrix[i][t]);

                }

            }

        }

    }

    det = 1;

    for(i = 0; i < n; i++){

        det =det* matrix[i][i];
    }
    if(det=-0){
        det=0;
    }
    printf("The determinant of matrix is: %d\n\n", det);

    return 0;
}

