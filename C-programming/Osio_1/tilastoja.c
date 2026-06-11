#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

double laske_pienin(double nums[], int koko)
{
	double ans = nums[0];
	int i;
	
	for (i=1;i<koko;++i) {
		ans = (ans < nums[i])? ans : nums[i];
	}
	return ans;
}

double laske_suurin(double nums[], int koko)
{
	double ans = nums[0];
	int i;
	
	for (i=1;i<koko;++i) {
		ans = (ans > nums[i]) ? ans : nums[i];
	}
	return ans;
}

int esiintymia(double a, double nums[], int koko) {
	int i;
	int ans = 0;
	
	for (i=0;i<koko;++i) {
		if (nums[i] == a) {++ans;}
	}
	return ans;
}

int main(int argc, char *argv[])
{
	double nums[SHRT_MAX];
	int koko = argc-1;
	int i;
	double pienin;
	double suurin;
	double ainut[SHRT_MAX];
	int ainut_koko = 0;
	double usein[SHRT_MAX];
	int usein_lkm = 0;
	int usein_koko = 0;
	int usein_lkm_apu = 0;
	
	for (i=1;i<argc;++i) {
		nums[i-1] = atof(argv[i]);
	}
	
	pienin = laske_pienin(nums, koko);
	suurin = laske_suurin(nums, koko);
	
	printf("Pienin: %f\n", pienin);
	printf("Suurin: %f\n", suurin);
	
	for (i=0;i<koko;++i) {
		if (esiintymia(nums[i], nums, koko) == 1) {
			ainut[ainut_koko] = nums[i];
			++ainut_koko;
		} else {continue;}
	}
	
	if (ainut_koko != 0) {
		printf("Ainutlaatuiset: ");
		for (i=0;i<ainut_koko;++i) {
			printf("%f", ainut[i]);
			if (i != ainut_koko-1) {printf(" ");}
			else {printf("\n");}
		}
	}
	
	for (i=0;i<koko;++i) {
		usein_lkm_apu = esiintymia(nums[i], nums, koko);
		if (i == 0 || usein_lkm_apu > usein_lkm) {
			usein_lkm = usein_lkm_apu;
			usein[0] = nums[i];
			usein_koko = 1;
		} else if (usein_lkm_apu == usein_lkm) {
			if (esiintymia(nums[i], usein, usein_koko) == 0){
				usein[usein_koko] = nums[i];
			    ++usein_koko;	
			}
		}
	}
	
	if (usein_lkm > 1) {
		printf("Useimmiten esiintyneet (%d kertaa): ", usein_lkm);
		for (i=0;i<usein_koko;++i) {
			printf("%f", usein[i]);
			if (i != usein_koko-1) {printf(" ");}
			else {printf("\n");}
		}
	}
	
	return 0;
}