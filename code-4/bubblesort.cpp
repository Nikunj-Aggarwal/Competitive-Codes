//Bubble sort
#include<iostream>
using namespace std;

int main()
{
	int a[100],n;
	cout<<"enter the number the elements \n";
	cin>>n;
	cout<<"enter the elements \n";
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		cout<<endl;
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<n-1;j++)
		{
			if(a[j]>a[j+1])
			{
				int c;
				c=a[j];
				a[j]=a[j+1];
				a[j+1]=c;
			}
		}
	}
	cout<<" the sorted array is \n";
	for(int i=0;i<n;i++)
	{
		cout<<a[i];
		cout<<endl;
     }
     return 0;
 }
