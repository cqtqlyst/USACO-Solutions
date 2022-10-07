import java.util.*;

public class Redistributing_Gifts {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[][] arr = new int[n][n];
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++) {
				arr[i][j] = scan.nextInt();
			}
		}
		Set<Integer> gifts = new HashSet<Integer>();
		int[] ans = new int[n];
		for (int i = 0; i<n; i++) {
			gifts.add(i+1);
		}
		boolean check = false;
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++) {
				if (gifts.contains(arr[i][j])) {
					/*if (j>0) {
						if (arr[i][j-1] == i+1) {
							check = true;
							break;
						}
					}
					*/
					ans[i] = arr[i][j];
					gifts.remove(arr[i][j]);
					break;
				}
			}
			/*
			if (check = true) {
				break;
			}
			*/
			
		}
		for (int i = 0; i<n; i++) {
			System.out.println(ans[i]);
		}
		
	}
	public static void solve() {
		
	}
}
