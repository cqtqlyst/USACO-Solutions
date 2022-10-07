import java.util.*;
import java.io.*;

public class Balancing_Stacks {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int sum = 0;
		int[] arr = new int[n];
		for (int i = 0; i<n; i++) {
			arr[i] = scan.nextInt();
			sum+=arr[i];
		}
		int target=sum/n;
		int ans = 0;
		for (int i = 0; i<n; i++) {
			if (arr[i]<=target) {
				ans+=target-arr[i];
			}
		}
		System.out.println(ans);
	}
}
