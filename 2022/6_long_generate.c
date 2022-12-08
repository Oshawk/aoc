#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define WINDOW_SIZE 60
#define LENGTH 2000000000

char character_set[] = {"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"};
char result[LENGTH] = {0};

int main() {

    srand(time(NULL));

    int insertion_point = rand() % (LENGTH - WINDOW_SIZE);

    for (int i = 0; i < WINDOW_SIZE; i++) {
        char character;

        do {
            character = character_set[rand() % (sizeof(character_set) - 1)];
        } while (memchr(&result[insertion_point], character, i) != NULL);

        result[insertion_point + i] = character;
    }

    for (int i = insertion_point - 1; i >= 0; i--) {
        char character;

        do {
            character = character_set[rand() % (sizeof(character_set) - 1)];
        } while (memchr(&result[i + 1], character, WINDOW_SIZE) == NULL);

        result[i] = character;
    }

    for (int i = insertion_point + WINDOW_SIZE; i < LENGTH; i++) {
        char character = character_set[rand() % (sizeof(character_set) - 1)];

        result[i] = character;
    }

    printf("%d\n", insertion_point + WINDOW_SIZE);

    FILE *f = fopen("6_long.txt", "w");
    fwrite(result, LENGTH, sizeof(result[0]), f);
    fclose(f);
}
