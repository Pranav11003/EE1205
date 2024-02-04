#include <stdio.h>

void generate_points(int max_n) {
    FILE *file = fopen("points.txt", "w");

    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    fprintf(file, "n,S(n)\n");
    
    for (int n = 0; n <= max_n; ++n) {
        int sequence_value = 12 + 4 * n;
        fprintf(file, "%d,%d\n", n, sequence_value);
    }

    fclose(file);
}

int main() {
    int max_n = 10;  // Adjust the maximum value of n as needed
    generate_points(max_n);

    return 0;
}
