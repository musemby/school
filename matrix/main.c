#include <stdio.h>

int initialmatrix[20][20],inputno;//initialize the array to store the elements
int determinant(int matrix[20][20],int a);//function prototype [function to find the determinant ]
int main()
{
  int i,j;//initialize the integer count
  printf("\n\nEnter order of matrix : ");
  scanf("%d",&inputno);
  printf("\nElements of matrix\n\n");
  for(i=1;i<=inputno;i++)
  {
  for(j=1;j<=inputno;j++)
  {
      //prompt the user to enter the matrix elements one by one
  printf("Enter row[%d] column[%d] = ",i,j);
  scanf("%d",&initialmatrix[i][j]);
  }
  }
  printf("\n\nMatrix obtained is \n");
  for(i=1;i<=inputno;i++)
     {
          printf("\n");
          for(j=1;j<=inputno;j++)
          {
               printf("\t%d \t",initialmatrix[i][j]);
          }
     }
  printf("\n \n");
  printf("\n Determinant of the Matrix  is: %d ", determinant(initialmatrix,inputno));
}//end main
//start of the function determinant [by cofactor expansion]
int determinant(int matrix[20][20],int sizeofmatrix)
{
  int entry_n,c[20],d=0,b[20][20],j,p,q,t;
  //for determinant of two by two matrix
  if(sizeofmatrix==2)
  {
    d=0;
    d=(matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1]);
    return(d);
   }
   //continues for more than two by two matrix

  else
  {
      //checks and compares with size of matrix
    for(j=1;j<=sizeofmatrix;j++)
    {
      int r=1,s=1;
//check no of rows to be less or equal to the one entered by user
      for(p=1;p<=sizeofmatrix;p++)
        {
//checks size of column in response to ones entered by users
        for(q=1;q<=sizeofmatrix;q++)
        {
            //delete row 1 column 1 to create a minor matrix
            if(p!=1&&q!=j)
        {
            b[r][s]=matrix[p][q];
                s++;
    //s stored in an array size to be subtracted by one..since arrays starts from zero
        if(s>sizeofmatrix-1)
                 {
                   r++;
                s=1;
            }
            }
            }
         }
//checking the sign i.e (+ or -) by multiplying -1 to the power 1+j times the minor matrix after removing row 1 and column j
    //calculate multiplier
     for(t=1,entry_n=1;t<=(1+j);t++)
     entry_n=(-1)*entry_n;
     c[j]=entry_n*determinant(b,sizeofmatrix-1);
     }
     //taking the sum of j=1 to n(number entered by user)
     for(j=1,d=0;j<=sizeofmatrix;j++)
     {
       d=d+(matrix[1][j]*c[j]);

      }
     return(d);
   }
}
