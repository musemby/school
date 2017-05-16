#include <stdio.h>

int N=20;

void getCofactor(int matrix[N][N], int temp[N][N], int p, int q, int n);
int determinantOfMatrix(int matrix[N][N], int order);

int main () {
	int order;
	printf("\nEnter the order of the matrix: ");
    scanf("%d", &order);
    N = order;
    int matrix[N][N];

    printf("\nEnter the elements of the matrix\n");
    for(int row=1;row<=order;row++){
        for(int col=1;col<=order;col++){
            printf("Element at [%d][%d] = ",row,col);
            scanf("%d",&matrix[row][col]);
        }
    }
    for(int i=1;i<=order;i++){
        for(int j=1;j<=order;j++)
            printf("\t%d ",matrix[i][j]);
        printf("\n");
    }
    printf("%d\n", determinantOfMatrix(matrix, order));

}

void getCofactor(int mat[N][N], int temp[N][N], int p, int q, int n)
{
    int i = 0, j = 0;
    printf("val of N--> %d\n", N);
 
    // Looping for each element of the matrix
    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {
            //  Copying into temporary matrix only those element
            //  which are not in given row and column [the submatrix]
            if (row != p && col != q)
            {
                temp[i][j++] = mat[row][col];
 
                // Row is filled, so increase row index and
                // reset col index
                if (j == n - 1)
                {
                    j = 0;
                    i++;
                }
            }
        }
    }
}

int determinantOfMatrix(int matrix[N][N], int order) {
	int D = 0; // Initialize result
 
    //  Base case : if matrix contains single element
    if (order == 1)
        return matrix[0][0];
 
    int temp[N][N]; // To store cofactors
 
    int sign = 1;  // To store sign multiplier
 
     // Iterate for each element of first row
    for (int f = 0; f < order; f++)
    {
        // Getting Cofactor of matrix[0][f]
        getCofactor(matrix, temp, 0, f, order);
        D += sign * matrix[0][f] * determinantOfMatrix(temp, order - 1);
 
        // terms are to be added with alternate sign
        sign = -sign;
    }
 
    return D;
}