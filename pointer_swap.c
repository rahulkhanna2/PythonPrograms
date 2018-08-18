#include <stdio.h>
#include <conio.h>



int swap (int*a , int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
    return 0;
}

int main(void)
{
    int x,y;
    x =25;
    y=32;
    int *p = &y;

    // *p will be used whenever we have to access the value
    // p will point out to the address of that value

    printf("Value of the address : %i\t Value of p is : %i\n",p,*p);
    printf("Values of X before swapping is %i\n",x);
    printf("Values of Y before swapping is %i\n",y);
    swap(&x,&y);
    printf("Values of X after swapping is %i\n",x);
    printf("Values of Y after swapping is %i\n",y);
}

