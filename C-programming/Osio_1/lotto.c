#include <stdio.h>
#include <stdlib.h>

int check_num(int a, int nums[], int size)
{
	int ans = 0;
	int i;
	for (i=0;i<size;++i) {
		if (nums[i]==a) {
			ans = 1;
			break;
		}
	}
    return ans;
}

int main(int argc, char *argv[])
{
	int voittorivi[7];
	int oma_rivi[7];
	int j;
	int oikein_t[7];
	int oikein = 0;
	
	for (j=0;j<argc-8;++j) {
		voittorivi[j] = atoi(argv[j+1]);
	}
	for (j=0;j<argc-8;++j) {
		oma_rivi[j] = atoi(argv[j+8]);
	}
	
	printf("Voittorivi: ");
	for (j=0;j<7;++j) {
		printf("%d",voittorivi[j]);
		
		if (j != 6) {printf(" ");}
		else {printf("\n");}
	}

    printf("Lottorivi: ");
	for (j=0;j<7;++j) {

		printf("%d",oma_rivi[j]);
		if (j != 6) {printf(" ");}
		else {printf("\n");}
	}
	
	for (j=0;j<7;++j) {
		if (check_num(oma_rivi[j], voittorivi, 7)) {
			oikein_t[oikein] = oma_rivi[j];
			++oikein;
		}
	}
	
	if (oikein == 0) {printf("Ei yhtään oikein!\n");}
	else {
		printf("%d oikein: ", oikein);
		for (j=0;j<oikein;++j) {
			printf("%d", oikein_t[j]);
			if (j != oikein-1) {printf(" ");}
			else{printf("\n");}
		}
	}
	
	return 0;
}