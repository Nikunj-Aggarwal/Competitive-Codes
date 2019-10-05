//Selection sort
#include<iostream>
using namespace std;

int main()
{
	int a[100],n,j;
	cout<<"enter the number the elements \n";
	cin>>n;
	cout<<"enter the elements \n";
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		cout<<endl;
	}
	for(int i=0;i<n;i++)
	{   int min=i;
		for(j=i+1;j<=n-1;j++)
		{
			if(a[min]>a[j])
			{  min=j;
				
			}	
			int c;
				c=a[i];
				a[i]=a[min];
				a[min]=c;
			
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
