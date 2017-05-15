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
#define BUFLEN 512  //Max length of buffer
#define PORT 8888   //The port on which to send data
 
void die(char *s)
{
    perror(s);
    exit(1);
}
 
int main(void)
{
    struct sockaddr_in si_other;
    int s, slen=sizeof(si_other);
    char buf[BUFLEN];
    char message[BUFLEN];
 
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
        die("sendto()");
    }
    if (sendto(s, matrix, sizeof(matrix) , 0 , (struct sockaddr *) &si_other, slen)==-1)
    {
        die("sendto()");
    }
     
    //receive a reply and print it
    //clear the buffer by filling null, it might have previously received data
    memset(buf,'\0', BUFLEN);
    //try to receive some data, this is a blocking call
    if (recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *) &si_other, &slen) == -1)
    {
        die("recvfrom()");
    }
     
    puts(buf);
 
    close(s);
    return 0;
}