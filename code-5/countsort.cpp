//Count sort
#include<iostream>

using namespace std;

int main()
{
  int a[1000]={0},n,i,j;
    cout<<"enter the number the elements \n";
	cin>>n;
	cout<<"enter the elements \n";
	for(i=0;i<n;i++)
	{   j=0;
		cin>>j;
		a[j]++;
		cout<<endl;
	}
	cout<<" the sorted array is \n";
	for(int k=0;k<n;k++)
	{   
		if(a[k]!=0)
		{
		 for(int x=0;x<a[k];x++)
		  {
			  cout<<k;
		   cout<<endl;}
     }
    } return 0;
 }
