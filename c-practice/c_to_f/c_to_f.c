#include <stdio.h>

/* print celsius to fahrenheit table */

int main()
{
	float fahrenheit, cels;
	float lower, upper, step;

	lower = -21.0;
	upper = 150.0;
	step = 10.0;
	
	cels = lower;
	while (cels <= upper) {
		fahrenheit = 9.0 * cels / 5.0 + 32.0;
		printf("%f\t%f\n", cels, fahrenheit);
		cels = cels + step;
	}
	return 0;
}


