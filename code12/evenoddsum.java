//even odd sum
package practice;

import java.util.Scanner;

public class evenoddsum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n, sum1 = 0, sum2 = 0, counter = 1;
		Scanner s = new Scanner(System.in);
		n = s.nextInt();
		while (n != 0) {
			if (counter % 2 == 0) {
				sum1 = sum1 + n % 10;
				n = n / 10;
			} else {
				sum2 = sum2 + n % 10;
				n = n / 10;
			}
			counter++;
		}
		System.out.println(sum2);
		System.out.println(sum1);
	}

}
