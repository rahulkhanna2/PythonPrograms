#include <stdio.h>

int main()
{
    int a[4] = {2,9,3,7};
    int *p,*r,*x,*y;
    //Different type of assignment, it always picks up the base address.
    p = a;
    y = &a[1];
    x = &a[2];
    r = &a[3];
    printf("Value of the first element is: %i\n",*p);

    // To show that array is continuos and int takes 4 bytes each
    printf("VAlue of the addresses are is : %i\n %i\n %i\n",y,x,r);
    int *q = a+1; // Another type of assignment
    printf("Value of the second element is: %i\n", *q);

return 0;
}
