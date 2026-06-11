#include <stdio.h>
#include <ctype.h>
#include <string.h>

int is_palindrome(char s[])
{
	int i = 0;
	int lippu = 1;
	int len = strlen(s);
	
	while (i<strlen(s)/2 && lippu) {
		if (tolower(s[i]) != tolower(s[len-i-1])) {
			return 0;
		}
		++i;
	}
	return 1;
}

int main(int argc, char *argv[])
{
	int i;
	
	for (i=1;i<argc;++i) {
		if (is_palindrome(argv[i])) {
			printf("\"%s\": on palindromi\n", argv[i]);
		} else {
			printf("\"%s\": ei ole palindromi\n", argv[i]);
		}
	}
	return 0;
}