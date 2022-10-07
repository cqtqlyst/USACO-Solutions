import java.util.*;

public class Email_Filing {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		int m;
		int n;
		int k;
		for (int i = 0; i<t; i++) {
			m = scan.nextInt();
			n = scan.nextInt();
			k = scan.nextInt();
			ArrayList<Integer> arr = new ArrayList<Integer>();
			int fn;
			for (int j = 0; j<n; j++) {
				fn = scan.nextInt();
				arr.add(j);
			}
			ArrayList<Integer>[] indicesof = new ArrayList[n];
			for (int j = 0; j<n; j++) {
				indicesof[j] = new ArrayList<Integer>();
				fn = arr.get(j);
				indicesof[fn].add(j);
			}
			for (int j = 0; j<n; j++) {
				
			}
			solve(m, n, k, arr);
		}
	}
	public static void solve(int m, int n, int k, ArrayList<Integer> arr) {
		
	}
}
