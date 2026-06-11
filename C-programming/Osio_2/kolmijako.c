#include "kolmijako.h"

IntPari kolmijako(unsigned int n, int t[], int vipu1, int vipu2, int *p1, int *p2) {
	int temp;
	unsigned int i;
    /* Vaihdetaan vipujen indeksit, jos t[vipu2] > t[vipu1] */
    if (t[vipu2] > t[vipu1]) {
        temp = vipu1;
        vipu1 = vipu2;
        vipu2 = temp;
    }

    int pienet1 = 0;
    int pienet2 = 0;

    for (i = 0; i < n; ++i) {
        if (t[i] < t[vipu1]) {
			temp = t[pienet1];
			t[pienet1] = t[i];
			t[i] = temp;
			if (vipu1 == pienet1) {
				vipu1 = i;
			}
			
			if (vipu2 == pienet1) {
				 vipu2 = i;
			}
			++pienet1;
		}
    }
	
	temp = t[pienet1];
	t[pienet1] = t[vipu1];
	t[vipu1] = temp;
	if(pienet1 == vipu2) {
		vipu2 == vipu1;
	}

    pienet2 = pienet1+1;
	
    for (i = pienet2; i < n; ++i) {
		if (t[i] < t[vipu2]) {
			temp = t[pienet2];
			t[pienet2] = t[i];
			t[i] = temp;
			
			if (vipu2 == pienet2) {
				 vipu2 = i;
			}
			++pienet2;
		}
    }
	
	temp = t[pienet2];
	t[pienet2] = t[vipu2];
	t[vipu2] = temp;

    /* Palautetaan tulokset */
    *p1 = pienet1;
    *p2 = pienet2;

    IntPari tulos;
    tulos.x = pienet1;
    tulos.y = pienet2;

    return tulos;
}