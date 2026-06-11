#include <string.h>
#include <math.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
	int ans = 0;
	int i;
	
	for (i = 0; i < strlen(argv[1]); ++i) {
		if (i == 0) {
			if (argv[1][i] == '1')
			ans -= pow(2,strlen(argv[1])-1);
		} else {
			if ( argv[1][i] == '1' )
			ans += pow(2,strlen(argv[1])-i-1);
		}
	}
	
	printf("%d\n", ans);
	return 0;
}