import java.util.*;

public class Cow_Frisbee {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		long sum = 0;
		int maxfn;
		sum+= (n-1)*2;
		int[] array = new int[n];
		for (int i = 0; i<n; i++) {
			array[i] = scan.nextInt();
		}
		for (int i = 0; i<n-3; i++) {
			maxfn = 0;
			for (int j = i+2; j<n; j++) {
				maxfn = Math.max(maxfn, array[j-1]);
				if (maxfn>array[i]) {
					break;
				}
				if (maxfn<array[j]) {
					sum += j-i+1;
				}
			}
		}
		System.out.println(sum);
	}
}
