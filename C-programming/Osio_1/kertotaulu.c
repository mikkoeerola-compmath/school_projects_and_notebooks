#include <stdio.h>

int main(void)
{
	int i;
	int j;
	
	for (i=0;i<16;++i) {
		for (j=0;j<16;++j) {
			if (j==0 && i==0) {printf("%4c",'x');}
			else if (i==0) {printf("%4d",j);}
			else if (j==0) {printf("%4d",i);}
			else {printf("%4d",j*i);}
		}
		printf("\n");
	}
	return 0;
}