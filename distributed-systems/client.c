#include <stdlib.h>
#include <stdio.h>
#include <strings.h> //bzero, bcopy
#include <unistd.h> // read, write
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

int matrix[20][20],order;

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
    int sockfd, portno, n, o, p;
    int temp, row, col, det=0;

    struct sockaddr_in serv_addr;
    struct hostent *server;

    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    validate_code(sockfd, "Sorry, there was an error creating the socket");

    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0) 
        throw_error("Sorry, there was an error establishing a connection");

    printf("\nEnter the order of the matrix: ");
    scanf("%d", &order);

    printf("\nEnter the elements of the matrix\n");
    for(row=1;row<=order;row++){
        for(col=1;col<=order;col++){
            temp = 0;
            printf("Element at [%d][%d] = ",row,col);
            scanf("%d",&matrix[row][col]);
        }
    }

    n = send(sockfd, &order, sizeof(order), 0);
    validate_code(n, "Sorry, there was an error writing to the socket");

    o = send(sockfd , matrix , sizeof(matrix), 0);
    validate_code(o, "Sorry, there was an error writing to the socket");
    
    p = recv(sockfd, &det, 2000, 0);
    validate_code(recv(sockfd, &det, 2000, 0), "Sorry, there was an error reading from the socket");
    printf("The determinant is: %d\n", det);

    return 0;
}
