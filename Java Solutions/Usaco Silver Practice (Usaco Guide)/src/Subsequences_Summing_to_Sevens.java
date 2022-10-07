import java.util.*;
import java.io.*;

public class Subsequences_Summing_to_Sevens {
	public static void main (String[] args) throws IOException {
		Scanner scan = new Scanner(new File("div7.in"));
		PrintWriter out = new PrintWriter(new File("div7.out"));
		int n = scan.nextInt();
		int[] prefix = new int[n+1];
		prefix[0]=0;
		int fn;
		for (int i = 1; i<n+1; i++) {
			fn = scan.nextInt();
			prefix[i] = (prefix[i-1] + fn)%7;
		}
		int[] first = new int[7];
		Arrays.fill(first, Integer.MAX_VALUE);
		int[] last = new int[7];
		Arrays.fill(last, -1);
		for (int i = 0; i<n+1; i++) {
			first[prefix[i]] = Math.min(i, first[prefix[i]]);
			last[prefix[i]] = i;
		}
		int max = 0;
		for (int i = 0; i<7; i++) {
			if (first[i] <= n) {
				max = Math.max (max, last[i] - first[i]);
			}
		}
		out.println(max);
		out.close();
		scan.close();
	}
}
