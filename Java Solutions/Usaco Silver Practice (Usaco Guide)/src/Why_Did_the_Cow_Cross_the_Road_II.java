import java.util.*;
import java.io.*;

public class Why_Did_the_Cow_Cross_the_Road_II {
	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(new File("maxcross.in"));
		PrintWriter out = new PrintWriter(new File("maxcross.out"));
		int n = scan.nextInt();
		int k = scan.nextInt();
		int b = scan.nextInt();
		int[] broken = new int[n+1];
		int fn = 0;
		for (int i = 0; i<b; i++) {
			fn = scan.nextInt();
			broken[fn]++;
		}
		int[] prefix = new int[n+1];
		for (int i = 0; i<n; i++) {
			prefix[i+1] = prefix[i] + broken[i+1];
		}
		int min = n+1;
		for (int i = 0; i<=n-k; i++) {
			min = Math.min(min, prefix[i+k] - prefix[i]);
		}
		out.println(min);
		out.close();
		scan.close();
	}
}
