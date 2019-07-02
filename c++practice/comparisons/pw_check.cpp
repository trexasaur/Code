#include <iostream>
#include <string>

using namespace std;

int main()
{
	string correct_pw = "sillygoose";
	string entered_pw;

	cout << "Please enter your password: ";
	getline(cin, entered_pw, '\n');
	if (entered_pw == correct_pw){
		cout << "Access granted!!\n";
	} else {
		cout << "Password is incorrect!!\n";
	}

	if (20398){
		cout << "numbers > 0 return True!\n";
	}

	return 0;
}