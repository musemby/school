#include <stdio.h>
 
// Dimension of input square matrix
#define N 20
 
// Function to get cofactor of mat[p][q] in temp[][]. n is current
// dimension of mat[][]
void getCofactor(int n, int mat[n][n], int temp[n][n], int p, int q)
{
    int i = 0, j = 0;
 
    // Looping for each element of the matrix
    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {
            //  Copying into temporary matrix only those element
            //  which are not in given row and column
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
 
/* Recursive function for finding determinant of matrix.
   n is current dimension of mat[][]. */
int determinantOfMatrix(int n, int mat[n][n])
{
    int D = 0; // Initialize result
 
    //  Base case : if matrix contains single element
    if (n == 1)
        return mat[0][0];
 
    int temp[n][n]; // To store cofactors
 
    int sign = 1;  // To store sign multiplier
 
     // Iterate for each element of first row
    for (int f = 0; f < n; f++)
    {
        // Getting Cofactor of mat[0][f]
        getCofactor(n, mat, temp, 0, f);
        D += sign * mat[0][f] * determinantOfMatrix( n - 1, temp);
 
        // terms are to be added with alternate sign
        sign = -sign;
    }
 
    return D;
}

 
// Driver program to test above functions
int main()
{
    /* int mat[N][N] = {{6, 1, 1},
                     {4, -2, 5},
                     {2, 8, 7}}; */
    int i, j, order;

    printf("Please enter the order of the matrix: \n");
    scanf("%d", &order);

    int matrix[order][order];

    printf("\nEnter the elements of the matrix\n");
    for(i=1;i<=order;i++){
        for(j=1;j<=order;j++){
            printf("Element at [%d][%d] = ",i,j);
            scanf("%d",&matrix[i][j]);
        }
    }
    for(int i=1;i<=order;i++){
            for(int j=1;j<=order;j++)
                printf("\t%d ",matrix[i][j]);
            printf("\n");
        }
 
    printf("Determinant of the matrix is : %d",
            determinantOfMatrix(order, matrix));
    return 0;
}
