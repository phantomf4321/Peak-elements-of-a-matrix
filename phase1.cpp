#include<iostream>

using namespace std;

//The steps of the algorithm are as follows :
//1 Receiving the matrix from the user
//2 The margin elements are equal to INT_MIN
//3 Each element is compared to all its adjacent elements
//4 confirmation variables will be equal to True for peaks
//5 All peak elements are printed

class matrix
{
private:
	long long int** data;
	int column, row;

	//confirmation for peak elements
	bool** confirm;

public:
	matrix(int c, int r) { column = c+2; row = r+2; }
	void make();
	void set();

	bool popup(int counter1, int counter2) { if (data[counter1][counter2] > data[counter1 - 1][counter2]) { return true; } }
	bool popright(int counter1, int counter2) { if (data[counter1][counter2] > data[counter1][counter2 + 1]) { return true; }}
	bool popdown(int counter1, int counter2) { if (data[counter1][counter2] > data[counter1 + 1][counter2]) { return true; }}
	bool popleft(int counter1, int counter2) { if (data[counter1][counter2] > data[counter1][counter2 - 1]) { return true; }}

	void check();
	void print();
};

void matrix::make()
{
	//make confirmation matrix
	confirm = new bool* [row];
	for (int i = 0; i < row; ++i)
		confirm[i] = new bool[column];

	//make matrix of informations
	data = new long long int* [row];
	for (int i = 0; i < row; ++i)
		data[i] = new long long int[column];

	//The margin elements are equal to INT_MIN
	for (int counter1 = 0; counter1 < row; counter1++)
		for (int counter2 = 0; counter2 < column; counter2++)
			if (counter1 == 0 || counter2 == 0 || counter1 == row - 1 || counter2 == column - 1)
				data[counter1][counter2] = INT_MIN;
}
void matrix::set()
{
	//make elements
	make();
	for (int counter1 = 1; counter1 <= row - 2; counter1++)
		for (int counter2 = 1; counter2 <= column - 2; counter2++)
		{
			//get elements of matrix from user
			cin >> data[counter1][counter2];
			//all the elements of confirmation arre equal to false
			confirm[counter1][counter2] = false;
		}
}
void matrix::check()
{
	//Each element is compared to all its adjacent elements
	for (int counter1 = 1; counter1 <= row - 2; counter1++)
		for (int counter2 = 1; counter2 <= column - 2; counter2++)
			if (popup(counter1, counter2) == true && popright(counter1, counter2) == true && popdown(counter1, counter2) == true && popleft(counter1, counter2) == true)
				confirm[counter1][counter2] = true;//confirmation variables will be equal to True for peaks
}
void matrix::print()
{
	//All peak elements are printed
	for (int counter1 = 1; counter1 < row - 1; counter1++)
		for (int counter2 = 1; counter2 < column - 1; counter2++)
			if (confirm[counter1][counter2])
				cout << data[counter1][counter2] << endl;
}


int main()
{
	int column, row;
	cin >> column >> row;
	matrix m1(column, row);
	m1.set();

	m1.check();
	m1.print();


	system("pause");
	return 0;
}
