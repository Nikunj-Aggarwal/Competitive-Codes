 //Question :
// TCS codevita Question 1
// find out till the same characters 

//solution:
#include <iostream>
using namespace std;
int main() {

	int t;
	cin>>t;
	while(t--){
		string x="";
		string p,s;
		cin>>p>>s;

		for(int i=0;i<p.length();i++){

			for(int j=0;j<s.length();j++){
				if(s[j]==p[i]){

					x=x+s[j];
					break;
				}

			}
		}
	cout<< x<<endl;
	}

return 0;
}


