#include <stdio.h>
int main(){
    int array[2][3]={0};
    int i,j;
   // printf("%-10s%-10s%-10s","custNo","bal bf","bal bf");
    for (i=0,j=0;i<sizeof(array);i++,j++){
        printf("%d  ",array[i][j]);
    }

return 0;
}
