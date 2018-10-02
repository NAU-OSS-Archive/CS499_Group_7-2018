/*
 *  File: conversionF1.c
 *
 *  Description: This file contains the characteristic and mantissa functions
 *      that can be used to get information about a floating point number.
 *      This program outputs a demonstration of these functions on the floating
 *      point number 123.456
 *
 *  Author: Christopher Ryan Combs Jr cc2668@nau.edu
 *     
 */

#include <stdbool.h>
#include <stdio.h>


// TODO: remove main method and create unit tests
int main() { 
    char number[] = "123.456";
    int c, n, d;

    // if the conversion from C string to integers can take place
    if(characteristic(number, &c) && mantissa(number, &n, &d)) {
        // do some math with c, n, and d
        printf("characteristic: %d, numerator: %d, denominator: %d\n", c, n, d);
    }
    else {
        // handle the error on input
        printf("oh no it broke");
    }
}


/*
 * Function: characteristic - searches a string for the characteristic of a float
 *
 * param: char numString[] - The string to be searched
 *        int *c - Where to store the output characteristic
 *
 * return: bool - True if run successfully
 *
 * TODO: add error handling for non-float characters and bad formatting
 */
bool characteristic(char numString[], int *c) {
        int count = 0;
        *c = 0;

        while(numString[count] != '.') {
                *c = (*c) * 10 + numString[count++] - '0';
        }
        return true;

}


/*
 * Function: mantissa - searches a string for the mantissa of a float
 *
 * param: char numString[] - The string to be searched
 *        int *numerator - Where to store the output numerator of the mantissa
 *        int *denominator - Where to store the output denominator of the mantissa
 *
 * return: bool - True if run successfully
 *
 * TODO: add error handling for non-float characters and bad formatting
 */
bool mantissa(char numString[], int *numerator, int *denominator) {
        int count = 0;
        *numerator = 0;
        *denominator = 1;

        while(numString[count++] != '.') {} // Start parsing at decimal point
        while(numString[count] != '\0') {
            *numerator = (*numerator) * 10 + numString[count++] - '0';
            *denominator *= 10;
        }
        return true;
}



