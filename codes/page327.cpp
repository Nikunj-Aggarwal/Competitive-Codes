//marks array

#include<iostream>
int main()
{
	int marks[2];
	int i;
	using namespace std;
    for(int i=0; i<2; i++)
    {
    	cout<<"enter the marks of student"<<i+1<<"\n";
    	cin>>marks[i];
	}
	cout<<"\n";
	for(i=0;i<2;i++ )
		cout<<"marks["<<i<<"]="<<marks[i]<<"\n";
		return 0;
}

