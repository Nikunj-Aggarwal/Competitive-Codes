//reverse number
package lecture1;

import java.util.Scanner;

public class reversenumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		  int n,i=0;
		  Scanner s=new Scanner(System.in);
		  n=s.nextInt();
		  
	while (n!=0) {
		int digit= n%10;
		i=i*10+digit;
		n=n/10;
		
	}
		  
		System.out.println(i);  
		
	}
}

