import java.util.*;
import java.io.*;

public class Triangles {
	static class coords {
		int x;
		int y;
	}
	static class compx implements Comparator<coords> {
		public int compare (coords one, coords two) {
			return Integer.compare(one.x, two.x);
		}
	}
	static class compy implements Comparator<coords> {
		public int compare (coords one, coords two ) {
			return Integer.compare(one.y, two.y);
		}
	}
	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(new File("triangles.in"));
		PrintWriter out = new PrintWriter(new File("triangles.out"));
		int n = scan.nextInt();
		coords[] arr = new coords[n];
		coords[] prefix = new coords[n];
		for (int i = 0; i<n; i++) {
			arr[i] = new coords();
			arr[i].x = scan.nextInt();
			arr[i].y = scan.nextInt();
		}
		Arrays.sort(arr, new compx());
		ArrayList<Integer> current = new ArrayList<Integer>();;
		int currentnum = arr[0].x;
		int startindex = 0;
		int s = 0;
		for (int i = 0; i<n; i++) {
			prefix[i] = new coords();
			if (arr[i].x!= currentnum) {
				for (int j = 0; j<current.size(); j++) {
					s += current.get(j) - current.get(0);
				}
				prefix[startindex].y = s;
				for (int j = 0; i<current.size()-1; j++) {
					prefix[startindex+j+1].y = prefix[startindex+j].y + (2*j)*(Math.abs(current.get(j+1) - current.get(j)));
				}
				currentnum = arr[i].x;
				startindex = i;
			}
			else {
				current.add(arr[i].y);
			}
		}
		Arrays.sort(arr, new compy());
		current.removeAll(current);
		currentnum = arr[0].y;
		startindex = 0;
		s = 0;
		for (int i = 0; i<n; i++) {
			if (arr[i].y!= currentnum) {
				for (int j = 0; j<current.size(); j++) {
					s += current.get(j) - current.get(0);
				}
				prefix[startindex].x = s;
				for (int j = 0; i<current.size()-1; j++) {
					prefix[startindex+j+1].x = prefix[startindex+j].x + (2*j)*(Math.abs(current.get(j+1) - current.get(j)));
				}
				currentnum = arr[i].y;
				startindex = i;
			}
			else {
				current.add(arr[i].y);
			}
		}
		long ans = 0;
		for (int i = 0; i<n; i++) {
			System.out.println(prefix[i].x + " " + prefix[i].y);
			ans += prefix[i].x * prefix[i].y;
			ans %= Math.pow(10, 9) + 7;
		}
		out.println(ans);
		scan.close();
		out.close();
	}
}
