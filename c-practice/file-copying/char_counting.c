#include <stdio.h>

/* counts chars in input; 1st version */

int main()
{
	long nc;

	nc = 0;
	while (getchar() != EOF)
		++nc;
	printf("%1ld\n", nc);
}
