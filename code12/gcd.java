// gcd
package practice;

import java.util.Scanner;

public class gcd {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n1, n2;
		Scanner s = new Scanner(System.in);
		n1 = s.nextInt();
		n2 = s.nextInt();

		while (n1 != n2) {
			if (n1 > n2)

				n1 = n1 - n2;
			else
				n2 = n2 - n1;
		}
		System.out.println(n2);
	}

}
