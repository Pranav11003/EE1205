#include <stdio.h>
#include <math.h>

// Function to calculate the derivative dy/dx
double derivative(double x, double y) {
    return 2 * x + y;
}

// Runge-Kutta method to solve the differential equation
void rungeKutta(double x0, double y0, double h, int n, FILE *file) {
    double x = x0, y = y0;

    for (int i = 0; i < n; i++) {
        fprintf(file, "%.4f %f\n", x, y);

        double k1 = h * derivative(x, y);
        double k2 = h * derivative(x + h / 2, y + k1 / 2);
        double k3 = h * derivative(x + h / 2, y + k2 / 2);
        double k4 = h * derivative(x + h, y + k3);

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        x = x + h;
    }
}

int main() {
    FILE *file;
    file = fopen("values.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Initial conditions
    double x0 = 0.0;
    double y0 = 1.0;

    // Step size and number of iterations (increase the number of iterations for more points between 0 and 1)
    double h = 0.01;
    int n = 100;

    // Apply Runge-Kutta method and save results to file
    rungeKutta(x0, y0, h, n, file);

    fclose(file);

    

    return 0;
}
