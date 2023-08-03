/* ------------------------------------------------------------------------
    RamseyNumbers_Recursive.c
        calculate the Ramsey number R(i, j) using recursive and
        mathematical rules from Ramsey theory.

    CSC 705
    Design & Analysis of Algorithms
    Dakota State University

    Kiera Conway

------------------------------------------------------------------------ */

#include <stdio.h>   // Standard Input/Output Library
#include <stdlib.h>  // Memory Allocation and Conversion Functions

/** ---------------------------- Constants ---------------------------- **/
#define MAX_INPUT 100

/** ---------------------------- Functions ---------------------------- **/
/*
 * Function:    RamseyNumber()
 *
 * Purpose:     Calculates the Ramsey number R(i, j) using recursion,
 *              the base cases, and three rules of Ramsey theory
 *
 * Parameters:  i - first parameter for the Ramsey number
 *              j - second parameter for the Ramsey number
 *
 * Return:      calculated Ramsey number R(i, j)
 */
int RamseyNumber(int i, int j){

    /* * * * * * * * * * * * * * * *
     * Base Case:
     *      R(i,1) = 1
     *      R(1,j) = 1
     * * * * * * * * * * * * * * * */
    if(i==1 || j==1){
        return 1;
    }

    /* * * * * * * * * * * * * * * *
     * Rule 1:
     *      R(i,2)=i
     *      R(2,j)=j
     * * * * * * * * * * * * * * * */
    if(i==2){
        return j;
    }
    if(j==2){
        return i;
    }

    /* Recursive Step */
    /* * * * * * * * * * * * * * * *
     * Rule 2:
     *      R(i,i) <= 4*R(i−2,i)+2
     * * * * * * * * * * * * * * * */
    int result, m, n;

    if (i==j){
        result = 4*RamseyNumber(i-2,j)+2;
    }
    else{
        m = RamseyNumber(i-1, j);
        n = RamseyNumber(i,j-1);


        /* * * * * * * * * * * * * * * * * * * * * * *
         * Rule 3:
         *      if R(i−1, j) and R(i, j−1) are even:
         *          R(i−1, j)+R(i, j−1)−1
         *      else:
         *          R(i−1, j)+R(i, j−1)
         * * * * * * * * * * * * * * * * * * * * * * */
        if (m%2 == 0 && n%2 == 0) {
            result = m + n - 1;
        }
        else{
            result = m + n ;
        }
    }

    /* Return Ramsey Result */
    return result;
}

/*
 * Function:    main()
 *
 * Purpose:     Entry point of the program
 *              Accepts user input for i and j, and calculates the Ramsey number R(i, j)
 *
 * Parameters:  argc - number of command-line arguments
 *              argv - array containing the command-line arguments
 *
 * Return:      -1 - invalid input parameters passed
 *               0 - successful execution
 */
int main(int argc, char *argv[]){

    /*
     * Program Initialization
     */
    int i, j;

    /*
     * Accept User Input
     */
    // Check if User Set Values on Command Line
    i = ( argc > 2 ? atoi(argv[1]) : -1);
    j = ( argc > 2 ? atoi(argv[2]) : -1);

    // if values not set, Prompt User
    if (i == -1){
        printf("Enter a value for i (1-100): ");
        fflush(stdout);
        scanf("%d", &i);
    }
    if (j == -1){
        printf("Enter a value for j (1-100): ");
        fflush(stdout);
        scanf("%d", &j);
    }

    // Verify Value Validity
    if (i < 1 || j < 1 || i > MAX_INPUT || j > MAX_INPUT) {
        printf("Invalid input. i and j should be positive integers up to %d.\n", MAX_INPUT);
        return -1;
    }

    printf("\nCalculating R(%d, %d)...\n", i, j);
    fflush(stdout);


    /*
     * Begin Ramsey Function Call
     */
    int result = RamseyNumber(i, j);

    /*
     * Function Termination
     */
    // Display Function Return Value
    printf("R(%d, %d) <= %d\n\n", i, j, result);
    printf("\"Every graph with %d vertices has a "
           "clique of size %d or an independent set of size %d.\"\n\n", result, i, j);

    return 0;
}