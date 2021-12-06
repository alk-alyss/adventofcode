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
	deque<int8_t> fish;
	while(pos = input.find(delimeter) != string::npos){
		string token = input.substr(0, pos);
		input.erase(0, pos+delimeter.length());
		fish.push_back(stoi(token));
	}
	fish.push_back(stoi(input));

	for(int i=0; i<256; i++){
		deque<int8_t> newFish;
		for(int j=0; j<fish.size(); j++){
			if(fish[j]==0){
				fish[j] = 6;
				newFish.push_back(8);
			}else{
				fish[j]--;
			}
		}
		fish.insert(fish.end(), newFish.begin(), newFish.end());
	}

	cout << fish.size() << endl;
}