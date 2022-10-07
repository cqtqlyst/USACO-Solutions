import java.util.*;

public class Subarray_Divisibility {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		long[] prefix = new long[n+1];
		int fn;
		prefix[0] = 0;
		for (int i = 1; i<n+1; i++) {
			fn=scan.nextInt();
			prefix[i] = (prefix[i-1] + fn) % n;
		}
		long[] mod = new long[n];
		long negative;
		for (int i = 0; i<n+1; i++) {
			negative = prefix[i];
			if (negative < 0) {
				negative = Math.abs(negative);
				negative = n - negative;
			}
			mod[(int) negative]+=1;
		}
		long ans = 0;
		long middle;
		for (int i = 0; i<n; i++) {
			if (mod[i]>1) {
				middle = mod[i] / 2 * (mod[i]-1);
				if (mod[i]%2 == 1) {
					middle += (mod[i]-1)/2;
				}
				ans += middle;
			}
		}
		System.out.println(ans);
	}
}
