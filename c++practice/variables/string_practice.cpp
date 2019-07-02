#include <iostream>
#include <string>

using namespace std;

int main()
{
	string first_name;
	string last_name;

	cout << "Please enter your first name: ";
	cin >> first_name;
	cout << "Please enter your last name: ";
	cin >> last_name;

	cout << "Your full name is " << first_name + " " + last_name << ".\n";

	return 0;
}