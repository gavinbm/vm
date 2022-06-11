#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum {HALT, ADD, MUL, SUB, OR, AND, NOT, SHL, SHR, MVI, LOAD, STORE,
      CMP, JNZ};

int isins(char *s) {
    char set[16][6] = {"halt", "add", "mul", "sub",
                       "or", "and", "not", "shl",
                       "shr", "mvi", "load", "store",
                       "cmp", "jnz"};
    
    for(int i = 0; i < 10; i++)
        if(strcmp(set[i], s) == 0)
            return i;
    
    return -1;
}

int main(int argc, char **argv) {

    FILE *read = fopen(argv[1], "r");
    char buffer[64], *tok;
    int len;

    while(fgets(buffer, 64, read) != NULL) {
        len = strlen(buffer);

        if(buffer[len - 1] == '\n')
            buffer[strlen(buffer) - 1] = '\0';

        tok = strtok(buffer, ", ");
        while(tok != NULL) {
            //printf("[%s]", tok);

            switch(isins(tok)) {
                case HALT:
                case ADD:
                case MUL:
                case SUB:
                case OR:
                case AND:
                case NOT:
                case SHL:
                case SHR:
                case MVI:
                case LOAD:
                case STORE:
                case CMP:
                case JNZ:
                default:
                    puts("what?");
                    exit(1);
            }
            tok = strtok(NULL, ", ");
        }
    }
    
    fclose(read);
    return 0;
} 