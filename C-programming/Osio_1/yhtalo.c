#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void ratkaise(double a, double b, double c, double ans[])
{
	double dis = b*b-4*a*c;
	
	if (dis < 0) {
		ans[0] = 0;
	} else if (dis == 0) {
		ans[0] = 1.0;
		ans[1] = (-b)/(2*a);
	} else {
		ans[0] = 2.0;
		ans[1] = (-b-sqrt(dis))/(2*a);
		ans[2] = (-b+sqrt(dis))/(2*a);
	}
}

int main(int argc, char *argv[])
{
	double a = atof(argv[1]);
	double b = atof(argv[2]);
	double c = atof(argv[3]);
	double ans[3];
	
	ratkaise(a,b,c, ans);
	
	if (ans[0] == 0) {
		printf("Ei ratkaisua\n");
	} else if (ans[0] == 1) {
		printf("%.3f\n", ans[1]);
	} else {
		printf("%.3f ", ans[1]<ans[2]?ans[1]:ans[2]);
		printf("%.3f\n", ans[1]>ans[2]?ans[1]:ans[2]);
	}
	
	return 0;
}