#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int main(int argc, char *argv[])
{
    int a = atoi(argv[1]);
	double nums[SHRT_MAX];
	int j;
	int i;
	double ans;
	for (j=0;j<argc-2;++j) {
		nums[j] = atof(argv[j+2]);
	}
	for (i=0; i<argc-2; ++i) {
		ans = sqrt(nums[i]);
		printf("sqrt(%.*f) = %.*f\n", a, nums[i], a, ans);
	}
	return 0;
}
