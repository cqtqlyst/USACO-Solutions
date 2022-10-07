import java.util.*;

public class Good_Subarrays {
	static long method (int n, String s) {
		int[] prefix = new int[n+1];
		for (int i = 1; i<n+1; i++) {
			prefix[i] = s.charAt(i - 1) - '0';
		}
		for (int i = 1; i<n+1; i++) {
			prefix[i]+=prefix[i-1];
		}
		HashMap<Integer, Long> map = new HashMap<>();
		for (int i = 0; i<n+1; i++) {
			if (map.containsKey(prefix[i] - i)) {
				map.put(prefix[i] - i, map.get(prefix[i] - i) + 1);
			}
			else {
				map.put(prefix[i] - i, (long) 1);
			}
		}
		long add = 0;
		long output = 0;
		for (int i : map.keySet()) {
			add = map.get(i);
			output += (add * (add-1)) / 2;
		}
		return output;
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String string;
		int queries = scan.nextInt();
		int arraylength;
		for (int i = 0; i<queries; i++) {
			arraylength = scan.nextInt();
			string = scan.next();
			System.out.println(method(arraylength, string));
		}
		
	}
}
