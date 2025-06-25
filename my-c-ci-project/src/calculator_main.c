#include <stdio.h>

#include "calculator_header.h"

int main() {
    double num1, num2, result;
    char op;

    printf("Simple Calculator\n");
    printf("Enter an expression (e.g., 2 + 2): ");
    scanf("%lf %c %lf", &num1, &op, &num2);

    switch(op) {
        case '+':
            result = add(num1, num2);
            break;
        case '-':
            result = subtract(num1, num2);
            break;
        case '*':
            result = multiply(num1, num2);
            break;
        case '/':
            if (num2 == 0) {
                printf("Error: Division by zero!\n");
                return 1;
            }
            result = divide(num1, num2);
            break;
        default:
            printf("Invalid operator!\n");
            return 1;
    }

    printf("Result: %.2lf\n", result);
    return 0;
}

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}


double divide(double a, double b) {
    return a / b;
}
