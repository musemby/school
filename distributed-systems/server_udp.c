#include <stdlib.h>
#include <strings.h> //bzero, bcopy
#include <unistd.h> // read, write
#include <stdio.h>
#include <sys/types.h> // types used in system calls
#include <sys/socket.h>
#include <netinet/in.h>

int matrix[20][20],order;

void keepalive(int); /* function prototype */

void validate_code(int code, char *msg)
{
    // Utility for throwing errors where the return code is a negative number
    if (code < 0) {
        perror(msg);
        exit(0);
    }
}

void throw_error(char *msg) {
    // Throws perror and exits with 1
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
    int sockfd, newsockfd, portno, clilen, pid;
    struct sockaddr_in serv_addr, cli_addr;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    validate_code(sockfd, "Sorry, there was an error creating the socket");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);
	
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);

    //bind function assigns details of the server to the socket.
    if (bind(sockfd, (struct sockaddr *) &serv_addr,
             sizeof(serv_addr)) < 0) 
             throw_error("Sorry, there was an error binding");
    listen(sockfd,5);
    clilen = sizeof(cli_addr);
    //run the server in an infinite loop to ensure that it is always running
    while (1) {
	
        newsockfd = accept(sockfd, 
              (struct sockaddr *) &cli_addr, &clilen);
        validate_code(newsockfd, "Sorry, there was an error accepting the connection");
        pid = fork();
        validate_code(pid, "Sorry, there was an error forking");
        if (pid == 0)  {
            close(sockfd);
            keepalive(newsockfd);
            exit(0);
         }
         else close(newsockfd);
     } /* end of while */
     return 0;
}

void keepalive (int sock)
{
/*
 continuously handle connections from clients
*/
   int n;
   n = read(sock,&order,sizeof(order));
   validate_code(n, "There was an error reading from socket");

   printf("The order of the matrix is: %d\n\n",order);
   n = read(sock,matrix,sizeof(matrix));
   for(int i=1;i<=order;i++){
        for(int j=1;j<=order;j++)
            printf("\t%d ",matrix[i][j]);
        printf("\n");
    }
   n = write(sock,"\n\nI got your message",18);
   validate_code(n, "Sorry, there was an error writing to the socket");
}
