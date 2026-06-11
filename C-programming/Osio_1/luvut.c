#include <stdio.h>

int main(void)
{
    int i=1;
    for (i=1; i<=100;++i) {
       if(i%2!=0 && i%3!=0 && i%5!=0){
		   printf("%d",i);
		   printf("%s",(i!=97)?" ":"");
	   }
    }
    printf("\n");
	return 0;
}