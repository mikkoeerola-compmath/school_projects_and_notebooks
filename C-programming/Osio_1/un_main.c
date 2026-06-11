#include <stdio.h>

int main()
{
	unsigned char i = 4;
	int j = 4;
	unsigned char a = -150;
	unsigned char b = 50;
	unsigned char temp = a;
	unsigned char temp_ed = 0;
	
	for (i=0; i == 0 || (temp_ed < temp && i<10);++i) {
		temp_ed = temp;
		temp = a+i*b;
		printf("%u ", temp_ed);
		printf("%u\n", temp);
	}
	if (a<b) {printf("JES");}
	return 0;
}