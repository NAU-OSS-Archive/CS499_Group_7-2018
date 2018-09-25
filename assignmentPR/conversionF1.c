#include <stdbool.h>
#include <stdio.h>

bool characteristic(char numString[], int *c) {
        int count = 0;
        *c = 0;

        while(numString[count] != '.') {
                *c = (*c) * 10 + numString[count++] - '0';
        }
        return true;

}

bool mantissa(char numString[], int *numerator, int *denominator) {
        int count = 0;
        *numerator = 0;
        *denominator = 1;

        while(numString[count++] != '.') {}
        while(numString[count] != '\0') {
            *numerator = (*numerator) * 10 + numString[count++] - '0';
            *denominator *= 10;
        }
        return true;
}

int main() {
    char number[] = "123.456";
    int c, n, d;

    // if the conversion from C string to integers can take place
    if(characteristic(number, &c) && mantissa(number, &n, &d))
    {
        // do some math with c, n, and d
        printf("characteristic: %d, numerator: %d, denominator: %d\n", c, n, d);
    }
    else
    {
        // handle the error on input
        printf("oh no it broke");
    }
}

