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
	int Wscore = Wuniv[9] + Wuniv[8] + Wuniv[7];
	int Kscore = Kuniv[9] + Kuniv[8] + Kuniv[7];

	cout << size <<" " << Wscore << " " << Kscore << "\n";

	return 0;
}