/*
    Simple udp client
*/
#include <stdio.h> //printf
#include <string.h> //memset
#include <stdlib.h> //exit(0);
#include <arpa/inet.h>
#include <sys/socket.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
 
#define SERVER "127.0.0.1"
#define PORT 8888   //The port on which to send data
 
void die(char *s)
{
    perror(s);
    exit(1);
}
 
int main(void)
{
    struct sockaddr_in si_other;
    int s, det, slen=sizeof(si_other);
 
    if ( (s=socket(AF_INET, SOCK_DGRAM, 0)) == -1)
    {
        die("socket");
    }
 
    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(PORT);
     
    if (inet_aton(SERVER , &si_other.sin_addr) == 0) 
    {
        fprintf(stderr, "inet_aton() failed\n");
        exit(1);
    }
 
    int order, i, j, n, matrix[20][20];

    printf("\nEnter the order of the matrix: ");
    scanf("%d", &order);

    printf("\nEnter the elements of the matrix\n");
    for(i=1;i<=order;i++){
        for(j=1;j<=order;j++){
            printf("Element at [%d][%d] = ",i,j);
            scanf("%d",&matrix[i][j]);
        }
    }

     
    //send the message
    if (sendto(s, &order, sizeof(order) , 0 , (struct sockaddr *) &si_other, slen)==-1)
    {
        die("Failed to send order of matrix");
    }
    if (sendto(s, matrix, sizeof(matrix) , 0 , (struct sockaddr *) &si_other, slen)==-1)
    {
        die("Failed to send the matrix");
    }
     
    if (recvfrom(s, &det, sizeof(det), 0, (struct sockaddr *) &si_other, &slen) == -1)
    {
        die("Failed to receive the determinant");
    }

    printf("The determinant of the matrix is: %d\n", det);
    
    close(s);
    return 0;
}