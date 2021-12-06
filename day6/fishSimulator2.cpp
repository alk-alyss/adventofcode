#include <iostream>
#include <deque>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream file ("input.txt");
	string input;
	if(file.is_open()){
		file >> input;
	}
	size_t pos;
	string delimeter = ",";
	long fish[9] = {0};
	while(pos = input.find(delimeter) != string::npos){
		string token = input.substr(0, pos);
		input.erase(0, pos+delimeter.length());
		fish[stoi(token)] += 1;
	}
	fish[stoi(input)] += 1;

	for(int i=0; i<256; i++){
		long temp = fish[0];
		for(int j=1; j<9; j++){
			fish[j-1] = fish[j];
		}
		fish[6] += temp;
		fish[8] = temp;
	}

	long result = 0;
	for(int i=0; i<9; i++){
		result += fish[i];
	}
	cout << result << endl;
}