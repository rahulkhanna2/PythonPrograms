#include <stdio.h>


int main(void)
{
    int i,least,j,temp,len;
    int num[] = {4,5,2,9,6,8,0,1,3};
    len= sizeof(num)/sizeof(num[0]);
    for(i=0;i<=len;i++)
        {
            least = i;
            for(j=i+1;j<len;j++)
            {
                    if (num[least]>num[j]){
                        least = j;
                    }
            }


             temp= num[i];
             num[i] = num[least];
             num[least] = temp;

        }
    for(int n=0;n<len;n++){
        printf("%i\n",num[n]);
    }
}
