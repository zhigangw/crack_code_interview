#include<vector>
#include<math.h>
#include<iostream>

#define _MAX(x,y) (x > y? x : y) 

using namespace std;

const int ROW = 10;
const int COL = 10;
const int BLOCKER = 0;

typedef struct {
	int row;
	int col;
	int value;
} path_node;

int a_grid[ROW][COL] = {
	{1,2,5,6,3,1,5,6,4,5},
	{3,2,5,6,0,0,5,6,4,5},
	{1,2,5,0,3,0,5,6,4,5},
	{1,2,5,6,0,1,5,6,4,5},
	{1,2,5,0,3,2,5,6,4,5},
	{1,2,5,0,3,3,5,6,4,5},
	{1,2,5,6,0,6,5,6,4,5},
	{1,2,5,6,3,9,5,0,4,5},
	{1,2,5,6,3,9,0,6,0,5},
	{1,2,5,0,3,0,5,6,4,5},
};

int compute_path_lengh(vector<path_node> list) {
	vector<path_node>::const_iterator iter;
	int max = 0;

	for (iter = list.begin(); iter < list.end(); iter++) {
		max += (*iter).value;
	}

	return max;
}

void print_path(vector<path_node> list) {
	for (size_t i = 0; i < list.size(); i++) {
		cout << i << ":" << list[i].row << ',' << list[i].col << ',' << list[i].value << "; ";
	}
	cout << endl;
}

bool has_end_point(vector<path_node> list, int n_r, int m_c) {
	size_t size = list.size();
	return  size > 0 && (list[size - 1]).col == m_c - 1 && (list[size - 1]).row == n_r - 1;
}

vector<path_node> get_path(int a[ROW][COL], int n_r, int m_c, int r, int c) {
	int max_r = 0;
	int max_c = 0;
	int max_t = 0;
	vector<path_node> list_path_r;
	vector<path_node> list_path_c;
	vector<path_node> list_path;

	if (c < m_c - 1 && a[r][c + 1] != BLOCKER) {
		list_path_c = get_path(a, n_r, m_c, r, c + 1);
	}
	if (r < n_r - 1 && a[r + 1][c] != BLOCKER) {
		list_path_r = get_path(a, n_r, m_c, r + 1, c);
	}
	max_r = has_end_point(list_path_r, n_r, m_c) ? compute_path_lengh(list_path_r) : 0;
	max_c = has_end_point(list_path_c, n_r, m_c) ? compute_path_lengh(list_path_c) : 0;

	max_t = a[r][c] + _MAX(max_r, max_c);
	if ((max_r > 0 || max_c > 0) || (r == n_r - 1) && (c == m_c - 1)) {
		list_path = max_c > max_r ? list_path_c : list_path_r;
		list_path.insert(list_path.begin(), { r, c, a[r][c] });
	}
	//cout << "r:" << r << ";c:" << c << ";max_t:" << max_t << endl;
	return list_path;
}

int robot_in_a_grid() {
	vector<path_node> list_path = get_path(a_grid, 10, 10, 0, 0);
	int max_l = compute_path_lengh(list_path);
	print_path(list_path);

	cout << endl << "max_l=" << max_l << endl;
	return max_l;
}