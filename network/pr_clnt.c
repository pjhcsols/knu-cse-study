#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <pthread.h>
#define BUF_SIZE 1000
#define NAME_SIZE 20

pthread_mutex_t mutx;
char name[NAME_SIZE] = "[DEFAULT]";
char message[BUF_SIZE];

void *send_message(void *arg);
void *recv_message(void *arg);
void error_handling(char *message);

int main(int argc, char *argv[]) {
    int sock;
    struct sockaddr_in serv_addr;
    pthread_t snd_thread, rcv_thread;
    void *thread_return;
    if (argc != 3) {
        printf("Usage : %s <IP> <port>\n", argv[0]);
        exit(1);
    }
    sock = socket(PF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr(argv[1]);
    serv_addr.sin_port = htons(atoi(argv[2]));

    if (connect(sock, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) == -1)
        error_handling("connect() error");
    pthread_mutex_init(&mutx, NULL);
    pthread_create(&snd_thread, NULL, send_message, (void *) &sock);
    pthread_create(&rcv_thread, NULL, recv_message, (void *) &sock);
    pthread_join(snd_thread, &thread_return);
    pthread_join(rcv_thread, &thread_return);
    close(sock);
    return 0;
}

void *send_message(void *arg) {
    int sock = *((int *) arg);
    while (1) {
        fgets(message, BUF_SIZE, stdin);
        if (!strcmp(message, "q\n") || !strcmp(message, "Q\n")) {
            close(sock);
            exit(0);
        } else if (!strcmp(message, "log\n")) {
            write(sock, message, strlen(message));
        } else {
            write(sock, message, strlen(message));
        }
    }
    return NULL;
}

void *recv_message(void *arg) {
    int sock = *((int *) arg);
    char name_message[NAME_SIZE + BUF_SIZE];
    int str_len;
    while (1) {
        pthread_mutex_lock(&mutx);
        str_len = read(sock, name_message, NAME_SIZE + BUF_SIZE - 1);
        pthread_mutex_unlock(&mutx);
        if (str_len == -1)
            return (void *) -1;
        name_message[str_len] = 0;
        if (name_message[0] == '[') {
            fputs(name_message, stdout);
        } else {
            FILE *fp = fopen("LOG", "w");
            if (fp == NULL) {
                perror("Failed to open LOG");
                exit(1);
            }
            fputs(name_message, fp);
            fflush(fp);
            fclose(fp);
            fp = fopen("LOG", "r");
            if (fp == NULL) {
                perror("Failed to open LOG");
                exit(1);
            }
            char ch;
            while ((ch = fgetc(fp)) != EOF) {
                putchar(ch);
            }
            fclose(fp);
        }
    }
    return NULL;
}

void error_handling(char *message) {
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}
