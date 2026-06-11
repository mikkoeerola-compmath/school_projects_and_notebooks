#include "caesar.h"
#include <stdio.h>

int main()
{
	char aakkosto[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char korvaavat[] = "OIUGENYMSWXVALPKHBQCZDFJRT";
	char mj[] = "OHJELMOINNIN TEKNIIKKA";
	
	caesarKoodaa(mj, aakkosto, korvaavat);
	
	printf("%s\n", mj);
	
	return 0;
}