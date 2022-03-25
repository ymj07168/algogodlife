#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main(void) {
	vector<int> Wuniv;
	vector<int> Kuniv;

	int score;
	for (int i = 0; i < 10; i++) {
		cin >> score;
		Wuniv.push_back(score);
	}
	for (int j = 0; j < 10; j++) {
		cin >> score;
		Kuniv.push_back(score);
	}

	sort(Wuniv.begin(), Wuniv.end());
	sort(Kuniv.begin(), Kuniv.end());


	int size = Wuniv.size();
	int Wscore = Wuniv[size-1] + Wuniv[size-2] + Wuniv[size-3];
	int Kscore = Kuniv[size-1] + Kuniv[size-2] + Kuniv[size-3];

	cout << size <<" " << Wscore << " " << Kscore << "\n";

	return 0;
}
