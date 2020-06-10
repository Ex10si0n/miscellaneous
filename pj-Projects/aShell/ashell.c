#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#ifdef _WIN32
#include <string.h>
static char buffer[2048];

char *readline(char *prompt){
    fputs(prompt, stdout);
    fgets(buffer, 2048, stdin);

    char *cpy = malloc(strlen(buffer)+1);

    strcpy(cpy, buffer);
    cpy[strlen(cpy) - 1] = '\0';

    return cpy;
}
void add_history(char* unused) {}

#else
#include <readline/readline.h>
#include <readline/history.h>
#endif
void cleanup_exit(int status) {
    clear_history();
    exit(status);
}
void prompt() {
    while (1) {
        char dirbuffer[1024];
        char *cwd = getcwd(dirbuffer, sizeof(dirbuffer));
        char *args[128];

        printf("⎧ [A-Shell] 📎 [%s]", cwd);
        char* command = readline("\n⎩ 🥑 says: ");
        args[0] = command;
        add_history(command);

        // Exit
        if (command == NULL || strcmp(command, "exit")==0) {
            cleanup_exit(EXIT_SUCCESS);
        }

        // Seperation of args
        int i;
        for (i = 0; *args[i]; i++)
            for (args[i+1] = args[i] + 1; *args[i+1]; args[i+1]++)
                if (*args[i+1] == ' ') {
                    *args[i+1] = '\0';
                    args[i+1]++;
                    break;
                }
        args[i] = NULL;
        if (!args[0]) continue;
        // Built-it Commands
        if (strcmp(args[0], "cd")==0) {
            int success = chdir(args[1]);
            if (success == -1){
                printf("[A-shell Error Called]: Directory Wrong As: %s\n", args[1]);
            }
        }

        // External Commands
        else {
          pid_t pid = fork();
          if (pid == 0) {
              execvp(args[0], args);
              printf("[A-shell Error Called]: Command Not Found: %s\n", args[0]);
          }
        }
        free(command);
        wait(NULL);
    }
}

int main(int argc, char** argv) {

    prompt();

    return EXIT_SUCCESS;
}
