#include "signaalit.h"
#include <setjmp.h>
#include <signal.h>

jmp_buf paluuTila;

void hoidaSIGFPE(int s) {
	signal(SIGFPE, hoidaSIGFPE);
	longjmp(paluuTila, SIGFPE);
}

void hoidaSIGSEGV(int s) {
	signal(SIGSEGV, hoidaSIGSEGV);
	longjmp(paluuTila, SIGSEGV);
}