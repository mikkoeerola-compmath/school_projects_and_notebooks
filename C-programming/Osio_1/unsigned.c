#include <stdio.h>
#include <limits.h>
#include "unsigned.h"

void ucharIntervalli(unsigned char sade, unsigned char askel) {
	unsigned char i;
	unsigned char temp = -sade;
	unsigned char temp_ed = 0;
	unsigned char temp_se = 0;
    printf("unsigned char:");
	
    for (i = 0; i == 0 || temp_ed < temp; ++i) {
		if (i!=0) {temp_ed = temp;}
		temp = -sade+i*askel;
		if (temp > sade && temp < -sade) {break;}
		printf(" %u", temp);
    }
	
	temp_se = temp + askel;

	while (temp_se <= sade && (temp <= temp_se)) {
		temp += askel;
		temp_se = temp + askel;
		printf(" %u", temp);
	}
	printf("\n");
}

void ushortIntervalli(unsigned short sade, unsigned short askel) {
	unsigned short i;
	unsigned short temp = -sade;
	unsigned short temp_ed = 0;
	unsigned short temp_se = 0;
    printf("unsigned short:");
	
    for (i = 0; i == 0 || temp_ed < temp; ++i) {
		if (i!=0) {temp_ed = temp;}
		temp = -sade+i*askel;
		if (temp > sade && temp < -sade) {break;}
		printf(" %u", temp);
		if (askel > 2*sade) {break;}
    }
	
	temp_se = temp + askel;
	
	while (temp_se <= sade && (temp <= temp_se)) {
		temp += askel;
		temp_se = temp + askel;
		printf(" %u", temp);
	}
	printf("\n");
}

void uintIntervalli(unsigned int sade, unsigned int askel) {
	unsigned int i;
	unsigned int temp = -sade;
	unsigned int temp_ed = 0;
	unsigned int temp_se = 0;
    printf("unsigned int:");
	
    for (i = 0; i == 0 || temp_ed < temp; ++i) {
		if (i!=0) {temp_ed = temp;}
		temp = -sade+i*askel;
		if (temp > sade && temp < -sade) {break;}
		printf(" %u", temp);
    }
	
	temp_se = temp + askel;
	
	while (temp_se <= sade && (temp <= temp_se)) {
		temp += askel;
		temp_se = temp + askel;
		printf(" %u", temp);
	}
    printf("\n");
}

void ulongIntervalli(unsigned long sade, unsigned long askel) {
	unsigned long i;
	unsigned long temp = -sade;
	unsigned long temp_ed = 0;
	unsigned long temp_se = 0;
    printf("unsigned long:");
	
    for (i = 0; i == 0 || temp_ed < temp; ++i) {
		if (i!=0) {temp_ed = temp;}
		temp = -sade+i*askel;
		if (temp > sade && temp < -sade) {break;}
		printf(" %lu", temp);
    }
	
	temp_se = temp + askel;
	
	while (temp_se <= sade && (temp <= temp_se)) {
		temp += askel;
		temp_se = temp + askel;
		printf(" %lu", temp);
	}
	printf("\n");
}