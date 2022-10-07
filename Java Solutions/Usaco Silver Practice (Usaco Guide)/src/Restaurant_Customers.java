import java.util.*;
import java.io.*;

public class Restaurant_Customers {
	static class Customer {
		int time;
		int pm;
	}
	static class Comp implements Comparator<Customer> {
		public int compare (Customer one, Customer two) {
			return Integer.compare(one.time, two.time);
		}
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		Customer[] data = new Customer[2*n];
		for (int i = 0; i<n; i++) {
			Customer c1 = new Customer();
			c1.time = scan.nextInt();
			c1.pm = 1;
			Customer c2 = new Customer();
			c2.time = scan.nextInt();
			c2.pm = -1;
			data[2*i] = c1;
			data[(2*i)+1] = c2;
		}
		Arrays.sort(data, new Comp());
		
		int sum = 0;
		int ans = 0;
		for (int i = 0; i<2*n; i++) {
			sum+=data[i].pm;
			ans = Math.max(ans, sum);
		}
		System.out.println(ans);
		scan.close();
	}
}
