#include <stdlib.h>
#include <stdio.h>


char getRandomChar() {
    return rand() % 256; 
}

int cypher(char *filename){
    FILE *inputFile, *cypherFile, *cypheredOutputFile;
    char character;

    srand(time(NULL)); 

    inputFile = fopen(filename, "r");

    if (inputFile == NULL) {
        printf("Error opening input file\n");
        return 1;
    }


    char outputFilename[100]; 
    sprintf(outputFilename, "cyphered%s", filename);


    cypherFile = fopen("cypher","w");
    cypheredOutputFile = fopen(outputFilename,"w");

    if (cypherFile == NULL || cypheredOutputFile == NULL) {
        printf("Error opening the file.\n");
        fclose(inputFile);
        if (cypherFile != NULL) fclose(cypherFile);
        if (cypheredOutputFile != NULL) fclose(cypheredOutputFile);
        return -1; 
    }



    char randomChar;
    while ((character = fgetc(inputFile)) != EOF) {
        randomChar = getRandomChar();
        fputc(randomChar, cypherFile);
        fputc(character ^ randomChar, cypheredOutputFile);
    }

    
    fclose(inputFile);
    fclose(cypherFile);
    fclose(cypheredOutputFile);

    return 0;
}


int main(){
    int result = cypher("bird.gif");
    if (result == 0) {
        printf("Encryption successful.\n");
    } else {
        printf("Encryption failed.\n");
    }
    return 0;
}