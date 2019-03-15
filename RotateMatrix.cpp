#include "iostream"
using namespace std;
constexpr int N = 4;
int A[N][N] = {
	{00,01, 02, 03},
	{10,11, 12, 13},
	{20,21, 22, 23},
	{30,31, 32, 33}
};

void print_matrix(int a[][N]) {
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++) {
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;

}
void rotate(int& a, int& b, int& c, int& d) {
	int t = a;
	a = b;
	b = c;
	c = d;
	d = t;
}

void rotate_matrix(int a[][N], int size) {
	print_matrix(a);
	for (int i = 0; i < size / 2; i++) {
		int d = N - 1 - i;
		for (int j = i; j < d; j++)
		{
			int r = i + j, c = i + j,r_d = d-j,c_d = d-j;

			rotate(a[i][c], a[r][d], a[d][c_d], a[r_d][i]);
			print_matrix(a);
		}
	}


}

void run_rotate_matrix() {
	rotate_matrix(A, N);
	rotate_matrix(A, N);
	rotate_matrix(A, N);
	rotate_matrix(A, N);
}