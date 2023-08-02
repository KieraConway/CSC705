
#include <stdio.h>
#include <stdlib.h>

#define MAX_INPUT 100

int RamseyNumber(int i, int j){
    /* Base Case */
    if(i==1 || j==1){
        return 1;
    }

    /* Rule 1:
     *      R(i,2)=i
     *      R(2,j)=j
     */
    if(i==2){
        return j;
    }
    if(j==2){
        return i;
    }

    /* Recursive Step */
    int result, m, n;

    /* Rule 2:
     *      R(i,i)<= 4*R(m−2,m)+2
     */
    if (i==j){
        result = 4*RamseyNumber(i-2,j)+2;
    }
    else{
        m = RamseyNumber(i-1, j);
        n = RamseyNumber(i,j-1);
        /* Rule 3:
         *      if R(i−1, j) and R(i, j−1) are even:
         *          R(i−1, j)+R(i, j−1)−1
         *
         *      else:
         *          R(i−1, j)+R(i, j−1)
         */
        if (m%2 == 0 && n%2 == 0) {
            result = m + n - 1;
        }
        else{
            result = m + n ;

        }
    }

    /* Return Value */
    return result;
}


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
