#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
	
	int i;
	for (i=1; i < argc; ++i) {
		/*unsigned int len = strlen(argv[i]);*/
		printf("%d: %s (pituus: %u)\n", i, argv[i], (unsigned int)strlen(argv[i]));
	}
	return 0;
}