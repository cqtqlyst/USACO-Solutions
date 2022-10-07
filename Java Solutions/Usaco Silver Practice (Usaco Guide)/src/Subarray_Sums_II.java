import java.util.*;

public class Subarray_Sums_II {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		int a;
		long prefix = 0;
		HashMap<Long, Integer> psums = new HashMap<>();
		psums.put((long) 0, 1);
		long answer = 0;
		for (int i = 0; i<n; i++) {
			a = sc.nextInt();
			prefix+=a;
			if (psums.containsKey(prefix - x)) {
				answer+= psums.get(prefix-x);
			}
			if (psums.containsKey(prefix) == false) {
				psums.put(prefix, 1);
			}
			else {
				psums.put(prefix, psums.get(prefix) + 1);
			}
		}
		System.out.println(answer);
	}
}
