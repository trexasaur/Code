#include <iostream>

using namespace std;

int main()
{
	double first_number, second_number;

	cout << "Let's divide numbers!\n";
	cout << "Please enter the first number: ";
	cin >> first_number;
	cout << "Please enter the second number: ";
	cin >> second_number;

	cout << "The answer to " << first_number << "/" << second_number << " is " << first_number/second_number << ".\n";

	return 0;
}