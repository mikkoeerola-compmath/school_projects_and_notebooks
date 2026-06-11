#include "muunto.h"
#include <ctype.h>
#include <string.h>

void muunna(char mj[])
{
	int i = 0;
    int j = strlen(mj) - 1;
	char temp;

    while (i <= j) {
		if (i==j) {
			mj[i] = isupper(mj[i]) ? tolower(mj[i]) : toupper(mj[i]);
		} else {
            mj[i] = isupper(mj[i]) ? tolower(mj[i]) : toupper(mj[i]);
            mj[j] = isupper(mj[j]) ? tolower(mj[j]) : toupper(mj[j]);

            temp = mj[i];
            mj[i] = mj[j];
            mj[j] = temp;
		}

        ++i;
        --j;
    }
}