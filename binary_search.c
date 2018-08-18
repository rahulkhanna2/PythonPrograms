#include <stdio.h>

int main(void)
{
    int i,j,low,high;
    int num[10] = {0,1,2,3,4,5,6,7,8,9};
    low = 0;
    high = 10;
    int mid = (low+high)/2;
    while (low<=high)
        {
            if(num[mid]>1)
                high = mid-1;
            else if(num[mid] == 1){
                printf("1 found at location: %d",mid+1);
                break;
            }
            else
                low = mid+1;
            mid = (low+ high)/2;
        }

}
