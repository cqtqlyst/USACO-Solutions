import java.util.*;
import java.io.*;
	
public class Connecting_Two_Barns {
	public static ArrayList<ArrayList<Integer>> adjlist;
	public static boolean visited[];
	public static int[] c1;
	public static int[] c2;
	public static void main (String[] args) {
		Scanner scan = new Scanner (System.in);
		int t = scan.nextInt();
		int m;
		int n = 0;
		int s;
		int e;
		int minfn;
		int maxfn;
		int ans = Integer.MAX_VALUE;
		int fn;
		int plus1;
		int minus1;
		ArrayList<Integer> connected1;
		ArrayList<Integer> connected2;
		for (int i = 0; i<t; i++) {
			n = scan.nextInt();
			m = scan.nextInt();
			connected1 = new ArrayList<Integer>();
			connected2 = new ArrayList<Integer>();
			visited = new boolean[n+1];
			adjlist = new ArrayList<ArrayList<Integer>>(n+1);
			for (int j = 0; j<n+1; j++) {
				adjlist.add(new ArrayList<Integer>());
			}
			c1 = new int[n+1];
			c2 = new int[n+1];
			for (int j = 0; j<m; j++) {
				s = scan.nextInt();
				e = scan.nextInt();
				adjlist.get(s).add(e);
				adjlist.get(e).add(s);
			}
			dfs1(1);
			if (c1[n] == 1) {
				System.out.println(0);
			}
			else {
				dfs2(n);
				for (int j = 1; j<n+1; j++) {
					if (c1[j] == 1)  {
						connected1.add(j);
					}
					if (c2[j] == 1) {
						connected2.add(j);
					}
				}
				Collections.sort(connected1);
				Collections.sort(connected2);
				minfn = connected2.get(0);
				maxfn = connected1.get(connected1.size()-1);
				connected2.add(connected1.get(connected1.size()-1));
				connected1.add(connected2.get(0));
				Collections.sort(connected1);
				Collections.sort(connected2);
				if (connected1.indexOf(minfn) == connected1.size() - 1) {
					plus1 = connected1.get(connected1.indexOf(minfn)-1);
				}
				else {
					plus1 = connected1.get(connected1.indexOf(minfn)+1);
				}
				if (connected1.indexOf(minfn) == 0) {
					minus1 = connected1.get(connected1.indexOf(minfn)+1);
				}
				else {
					minus1 = connected1.get(connected1.indexOf(minfn)-1);
				}
				ans = Math.min((plus1 - minfn) * (plus1 - minfn), ans);
				System.out.println(ans);
				ans = Math.min(ans, (minfn - minus1) * (minfn - minus1));
				System.out.println(ans);
				if (connected2.indexOf(maxfn) == connected2.size() - 1) {
					plus1 = connected2.get(connected2.indexOf(maxfn)-1);
				}
				else {
					plus1 = connected2.get(connected2.indexOf(maxfn)+1);
				}
				if (connected2.indexOf(maxfn) == 0) {
					minus1 = connected2.get(connected2.indexOf(maxfn)+1);
				}
				else {
					minus1 = connected2.get(connected2.indexOf(maxfn)-1);
				}
				ans = Math.min((plus1 - minfn) * (plus1 - minfn), ans);
				System.out.println(ans);
				ans = Math.min(ans, (minfn - minus1) * (minfn - minus1));
				System.out.println(ans);
			}
			
		}
		scan.close();
	}
	public static void dfs1(int x) {
		if (visited[x]) {
			return;
		}
		c1[x] = 1;
		visited[x] = true;
		for (int i: adjlist.get(x)) {
			if (!visited[i]) {
				dfs1(i);
			}
		}
	}
	public static void dfs2(int x) {
		if (visited[x]) {
			return;
		}
		c2[x] = 1;
		visited[x] = true;
		for (int i: adjlist.get(x)) {
			if (!visited[i]) {
				dfs2(i);
			}
		}
	}
}
