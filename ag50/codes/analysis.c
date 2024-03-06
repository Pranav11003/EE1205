#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Define the range of x values
    double start_x = -5.0;
    double end_x = 5.0;
    double step = 0.1;

    // Calculate and store the values in the file
    for (double x = start_x; x <= end_x; x += step) {
        double result = 3 * exp(x) - 2 * (x + 1);
        fprintf(file, "%.2f %f\n", x, result);
    }

    fclose(file);


    return 0;
}
