#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	char a = atoi(argv[1]);
	char b = atoi(argv[2]);
	char i;
	for (i = a; i <= b; ++i)
	{
		printf("%d: %c\n", i, i);
		if ( i == CHAR_MAX) {break;}
	}
	return 0;
}