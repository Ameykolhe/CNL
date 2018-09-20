#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<netdb.h>
#define MAXLEN 65535
#define PORT 8099
#define PI 3.142

void main(){

	int server_fd, sock_fd;
	struct sockaddr_in address;
	int opt = 1;
	int addrlen = sizeof(address);

	if( (server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
	{
		perror("socket failed");
        exit(EXIT_FAILURE);
	}

	if( setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,&opt, sizeof(opt)))
	{
		perror("setsockopt");
        exit(EXIT_FAILURE);
	}

	memset(&address, 0, addrlen);
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);

	if (bind(server_fd, (struct sockaddr *)&address,sizeof(address))<0)
   	{
        	perror("bind failed");
        	exit(EXIT_FAILURE);
   	}

    if(listen(server_fd, 3) < 0)
    {
    	perror("listen");
    	exit(EXIT_FAILURE);
    
	}
    if ((sock_fd = accept(server_fd, (struct sockaddr *)&address,(socklen_t*)&addrlen))<0)
   	{
        perror("accept");
        exit(EXIT_FAILURE);
    }

	int len;

/*
	//Message Transfer

	char buffer[MAXLEN];

    len = read(sock_fd, buffer, MAXLEN);
    printf("%s\n", buffer);

*/

	//File transfer
	
	char fileName[256];

	len = read(sock_fd, fileName, MAXLEN);
	FILE *fp;
	fp = fopen( &fileName, "w+");
	char buffer2[MAXLEN];
	len = read(sock_fd, buffer2, MAXLEN);
	fprintf(fp, "%s", buffer2);
	fclose(fp);

/*

	// Trigonometric Calculator
	int recv, option, num1, num2, answer;
	len = read(sock_fd, &recv, sizeof(recv));
	option = ntohl(recv);
	len = read(sock_fd, &recv, sizeof(recv));
	num1 = ntohl(recv);
	len = read(sock_fd, &recv, sizeof(recv));
	num2 = ntohl(recv);

	//printf("%d, %d, %d", option, num1, num2);

	switch(option){
		case 1:
			answer = num1 + num2;
			break;
		case 2:
			answer = num1 - num2;
			break;
		case 3:
			answer = num1 * num2;
			break;
		case 4:
			answer = num1 / num2;
			break;
		default:
			answer = 0;
			break;
	}

	recv = htonl(answer);
	send(sock_fd, &recv, sizeof(recv), 0);

*/

}
