#include <stdio.h>
#include <stdlib.h>


void count_bits(int val){
    int mask = 1;
    int count_ones = 0;
    int num_of_bits = sizeof(val)*8;
    for(int i = 0; i < num_of_bits;i++){
        if(mask & val) count_ones++;
        mask <<= 1;
    }
    printf("%d zeros e %d uns \n", num_of_bits - count_ones, count_ones);
}


void print_fibonacci(int N) {
    if(N < 0){ 
        printf("N inválido");
        return;
    };
    int a = 0, b = 1;
    printf("Sequência de Fibonacci para os primeiros %d termos:\n", N);
    for (int i = 0; i < N; i++) {
        printf("%d ", a);
        int next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
}




int file_symbol_freq(char *file_name, char symbol) {
    FILE *file = fopen(file_name, "r");
    if (file == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return -1;
    }

    int frequency = 0;
    int ch;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == symbol) {
            frequency++;
        }
    }

    fclose(file);
    printf("frequency = %d", frequency);
    return frequency;
}



void file_histogram(char *file_name) {
    FILE *file = fopen(file_name, "r");
    if (file == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return;
    }

    int frequencies[256] = {0}; // Assumindo que estamos lidando com caracteres ASCII

    int ch;
    while ((ch = fgetc(file)) != EOF) {
        frequencies[ch]++;
    }

    printf("Histograma do arquivo %s:\n", file_name);
    for (int i = 0; i < 256; i++) {
        if (frequencies[i] > 0) {
            printf("'%c': %d\n", (char)i, frequencies[i]);
        }
    }

    fclose(file);
}



void reverse_file(char *input_file_name, char *output_file_name) {
    // Abrir o arquivo de entrada para leitura
    FILE *input_file = fopen(input_file_name, "r");
    if (input_file == NULL) {
        perror("Erro ao abrir o arquivo de entrada");
        return;
    }

    // Abrir o arquivo de saída para escrita
    FILE *output_file = fopen(output_file_name, "w");
    if (output_file == NULL) {
        perror("Erro ao criar o arquivo de saída");
        fclose(input_file);
        return;
    }

    // Mover o ponteiro para o final do arquivo de entrada
    fseek(input_file, 0, SEEK_END);
    long size = ftell(input_file);

    // Ler o arquivo de entrada de trás para frente e escrever no arquivo de saída
    for (long i = size - 1; i >= 0; i--) {
        fseek(input_file, i, SEEK_SET);
        char c = fgetc(input_file);
        if (c != EOF) {
            fputc(c, output_file);
        }
    }

    // Fechar os arquivos
    fclose(input_file);
    fclose(output_file);
}

int main() {
    count_bits(8);
    print_fibonacci(6);


    file_symbol_freq("a.txt", 'a');
    file_histogram("a.txt");
    // Chamada da função para reverter o arquivo
    reverse_file("a.txt", "output.txt");

    printf("Arquivo revertido com sucesso.\n");

    return 0;
}



