#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#define BUF_SIZE 100

#define NAME_SIZE 50
#define COUNTRY_SIZE 50
#define CLNT_MAX_in 256

struct user_info{
    char name[NAME_SIZE];
    char country[COUNTRY_SIZE];
    int age;
};FILE *user_infos_fp;

pthread_mutex_t mutx;
pthread_mutex_t mutx_io;
int clnt_cnt = 0;
int clnt_socks[CLNT_MAX_in];

void * handle_clnt(void * arg);
void send_message(char * name, char * message);
void send_log(int sock);
void error_handling(char * message);

int main(int argc, char *argv[]){
    int serv_sock, clnt_sock;
    struct sockaddr_in serv_adr, clnt_adr;
    socklen_t clnt_adr_sz;
    pthread_t t_id;
    if(argc != 2){
        printf("Usage: %s <port>\n", argv[0]);
        exit(1);
    }
    
    pthread_mutex_init(&mutx, NULL);
    pthread_mutex_init(&mutx_io,NULL);
    serv_sock = socket(PF_INET, SOCK_STREAM, 0);
    
    memset(&serv_adr, 0, sizeof(serv_adr));
    serv_adr.sin_family = AF_INET;
    serv_adr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_adr.sin_port = htons(atoi(argv[1]));
    
    if(bind(serv_sock, (struct sockaddr*) &serv_adr, sizeof(serv_adr)) == -1)
        error_handling("bind() error");
    if(listen(serv_sock, 5) == -1)
        error_handling("listen() error");
        
    user_infos_fp = fopen("USER_INFO", "w");
    if(user_infos_fp == NULL)
        error_handling("USER_INFO file_open() error");
    
    
    while(1){
        clnt_adr_sz = sizeof(clnt_adr);
        clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_adr, &clnt_adr_sz);
        
        pthread_mutex_lock(&mutx);
        clnt_socks[clnt_cnt++]=clnt_sock;
        pthread_mutex_unlock(&mutx);
        
        pthread_create(&t_id, NULL, handle_clnt, (void*)&clnt_sock);
        pthread_detach(t_id);
        printf("Connected client IP: %s \n", inet_ntoa(clnt_adr.sin_addr));
    }
    close(serv_sock);
    return 0;
}

void * handle_clnt(void * arg){
    int clnt_sock = *((int*)arg);
    int str_len = 0,i;
    char message[BUF_SIZE];
    char hello_message[] = "[sys] : Welcome to the Chat ROOM. write information -> [NAME] [AGE] [COUNTRY]\n";
    char info_error_message[] = "[sys] : Information error. Try again : [NAME] [AGE] [COUNTRY]\n";
    struct user_info info_input;
    
    pthread_mutex_lock(&mutx);
    write(clnt_sock, hello_message, strlen(hello_message));
    pthread_mutex_unlock(&mutx);
    
    while(1){
        str_len = read(clnt_sock, message, sizeof(message));
        message[str_len-1] = '\0';
        if(str_len == -1){
            pthread_mutex_lock(&mutx);
            write(clnt_sock, info_error_message, strlen(info_error_message));
            pthread_mutex_unlock(&mutx);
        }
        else if(sscanf(message, "%49s %d %49s", info_input.name, &info_input.age, info_input.country) != 3){
            pthread_mutex_lock(&mutx);
            write(clnt_sock, info_error_message, strlen(info_error_message));
            pthread_mutex_unlock(&mutx);
        }
        else{
            pthread_mutex_lock(&mutx_io);
            fprintf(user_infos_fp,"%s %d %s\n", info_input.name, info_input.age, info_input.country);
            fflush(user_infos_fp);
            pthread_mutex_unlock(&mutx_io);
            break;
        }
    }
    sprintf(message, "[%s] joins to chatting ROOM!, Total [%d] in chatting ROOM", info_input.name, clnt_cnt);
    send_message("ADMIN", message);

    
    while((str_len = read(clnt_sock, message, sizeof(message))) != 0){
        message[str_len-1] = '\0';
        if(!strcmp(message, "log")){
            send_log(clnt_sock);
            continue;
        }
        send_message(info_input.name, message);
    }
    
    pthread_mutex_lock(&mutx);
    for(i = 0; i < clnt_cnt; i++){
        if(clnt_sock == clnt_socks[i]){
            while(i++<clnt_cnt-1)
                clnt_socks[i]=clnt_socks[i+1];
            break;
        }
    }
    clnt_cnt--;
    pthread_mutex_unlock(&mutx);
    close(clnt_sock);
    sprintf(message, "[%s] lefts chatting ROOM!, Total [%d] in chatting ROOM", info_input.name, clnt_cnt);
    send_message("ADMIN", message);
    return NULL;
}

void send_message(char *name, char *message){
    int i;
    char name_message[NAME_SIZE + BUF_SIZE];
    sprintf(name_message,"[%s] : %s\n", name, message);
    pthread_mutex_lock(&mutx);
    for(i=0; i<clnt_cnt; i++)
        write(clnt_socks[i], name_message, strlen(name_message));
    pthread_mutex_unlock(&mutx);
}

void send_log(int sock){
    FILE *fp = fopen("USER_INFO", "r");
    char buf[BUF_SIZE];
    pthread_mutex_lock(&mutx);
    while (fgets(buf, BUF_SIZE, fp) != NULL){
        write(sock, buf, strlen(buf));
    }
    pthread_mutex_unlock(&mutx);
    fclose(fp);
}



void error_handling(char *message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}