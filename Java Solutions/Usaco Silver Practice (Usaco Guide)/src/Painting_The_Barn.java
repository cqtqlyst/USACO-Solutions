import java.util.*;
import java.io.*;

public class Painting_The_Barn {
	public static void main (String[] args) throws IOException {
		Scanner sc = new Scanner(new File("paintbarn.in"));
		PrintWriter out = new PrintWriter(new File("paintbarn.out"));
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[][] arr = new int[1001][1001];
		int a, b, c, d;
		for (int i = 0; i<n; i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			c = sc.nextInt();
			d = sc.nextInt();
			arr[a][b]++;
			arr[c][d]++;
			arr[a][d]--;
			arr[c][b]--;
		}
		int ans = 0;
		for (int i = 0; i<1001; i++) {
			for (int j = 0; j<1001; j++) {
				if (i>0) {
					arr[i][j] += arr[i-1][j];
				}
				if (j>0) {
					arr[i][j] += arr[i][j-1];
				}
				if (i>0 && j>0) {
					arr[i][j] -= arr[i-1][j-1];
				}
				if (arr[i][j] == k) {
					ans++;
				}
			}
		}
		out.println(ans);
		sc.close();
		out.close();
	}
}
