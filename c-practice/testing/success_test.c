#include <stdio.h>


int test_function()
{
	int EGADS_SUCCESS = "EGADS_SUCCESS";
	return EGADS_SUCCESS;
}

int main()
{
	int EGADS_SUCCESS = "EGADS_SUCCESS";
	int value;
	value = test_function();
	if (value == EGADS_SUCCESS) {
		printf("Yup, it worked");
	}
}
