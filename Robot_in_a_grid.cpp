#include<vector>
#include<math.h>
#include<iostream>

#define _MAX(x,y) (x > y? x : y) 

using namespace std;

const int ROW = 10;
const int COL = 10;
const int BLOCKER = 0;

int a_grid[ROW][COL] = {
	{1,2,5,6,3,0,5,6,4,5},
	{3,2,5,6,0,0,5,6,4,5},
	{1,2,5,0,3,0,5,6,4,5},
	{1,2,5,6,0,1,5,6,4,5},
	{1,2,5,0,3,2,5,6,4,5},
	{1,2,5,0,3,3,5,6,4,5},
	{1,2,5,6,0,6,5,6,4,5},
	{1,2,5,6,3,9,5,0,4,5},
	{1,2,5,6,3,9,5,6,0,5},
	{1,2,5,0,3,1,5,6,4,5},
};

int max_path = 0;
vector<int> path_list;
int get_path(int a[ROW][COL], int n_r, int m_c, int r,  int c){
	int max_r = 0;
	int max_c = 0;
	int max_t = 0;
	if (c < m_c - 1 && a[r][c + 1] != BLOCKER) {
		max_c = get_path(a, n_r, m_c,  r, c + 1);
	}
	if (r < n_r - 1 && a[r + 1][c] != BLOCKER) {
		max_r = get_path(a, n_r, m_c, r + 1, c);
	}

	max_t = a[r][c] + _MAX(max_r, max_c);

	cout << "r:" << r << ";c:" << c << ";max_t:" << max_t<<endl; 
	return max_t;
}

int robot_in_a_grid() {
	int max_t = get_path(a_grid, 10, 10, 0, 0);
	int max_l = 0;

	vector<int>::const_iterator iter;
	for(iter = path_list.begin(); iter!=path_list.end();iter++)
	{
		max_l += *iter;
		cout << *iter <<",";
	}

	cout <<endl <<"max_t=" <<max_t <<",max_l="<< max_l<<",max_path=" << max_path << endl;
	return max_path;
}