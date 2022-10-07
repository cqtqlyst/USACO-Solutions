import java.util.*;
import java.io.*;

public class GCD_on_BlackBoard {
	public static long gcd(long n1, long n2) {
		if (n2 == 0) {
			return n1;
		}
		return gcd(n2, n1%n2);
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner (System.in);
		int n = scan.nextInt();
		int[] array = new int[n+1];
		for (int i = 0; i<n; i++) {
			array[i]=scan.nextInt();
		}
		long[] left = new long[n+2];
		long[] right = new long[n+2];
		for (int i = 1; i<=n; i++) {
			left[i] = gcd(left[i-1], array[i]);
		}
		for (int i = n; i>=1; i--) {
			right[i] = gcd(right[i+1], array[i]);
		}
		long max = 0;
		for (int i = 1; i<=n; i++) {
			max = Math.max(max, gcd(right[i+1], left[i-1]));
		}
		System.out.println(max);
		
	}
}