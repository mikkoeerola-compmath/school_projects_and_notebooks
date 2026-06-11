#include <stdio.h>
#include <stdlib.h>

int calculate_space(int b, int d)
{
	int num = b*d;
	int ans = 0;
	
	while (num != 0) {
		num = num/10;
		ans +=1;
	}
	return ans;
}

int main(int argc, char *argv[])
{
	int a = atoi(argv[1]);
	int b = atoi(argv[2]);
	int c = atoi(argv[3]);
	int d = atoi(argv[4]);
	int space;
	int i;
	int j;
	
	space = calculate_space(b, d)+1;
	
	for (j=c-1;j<=d;++j) {
		for (i=a-1;i<=b;++i) {
			if (j<c && i<a) {printf("%*s", space, "");}
			else if (i<a) {printf("%*d", space, j);}
			else if (j<c) {printf("%*d", space, i);}
			else {printf("%*d",space,j*i);}
		}
		printf("\n");
	}
	return 0;
}