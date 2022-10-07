import java.util.*;


public class Robot_Instructions {
	static coords[] array;
	static coords target;
	static int[] ans;
	static coords[] prefix;
	static class coords{
		int x;
		int y;
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		array = new coords[n];
		target = new coords();
		ans = new int[n+1];
		target.x = scan.nextInt();
		target.y = scan.nextInt();
		prefix = new coords[n];
		for (int i = 0; i<n; i++) {
			array[i] = new coords();
			array[i].x = scan.nextInt();
			array[i].y = scan.nextInt();
			prefix[i] = new coords();
			if (i == 0) {
				prefix[i].x = array[i].x;
				prefix[i].y = array[i].y;
			}
			else {
				prefix[i].x = prefix[i-1].x + array[i].x;
				prefix[i].y = prefix[i-1].y + array[i].y;
			}
		}
		for (int i = 0; i<n; i++) {
			System.out.println(prefix[i].x + " " + prefix[i].y);
		}
		recursion(0, 0, 0, 0, n);
		for (int i = 0; i<n; i++) {
			System.out.println(ans[i]);
		}
	}
	public static void recursion(int sumx, int sumy, int index, int sizeofyes, int num) {
		if (index == num) {
			if (sumx == target.x && sumy == target.y) {
				ans[sizeofyes-1]++;
			}
			return;
		}
		//pruning
		//the below attempt at pruning by prefix doesn't work at all
		/*
		if (index>0) {
			if (sumx>target.x) {
				
				if (sumx + prefix[num-1].x - prefix[index-1].x > target.x) {
					//System.out.println(sumx + " " + sumy + " num: " + sizeofyes + "stopped by sumx>");
					//return;
				}
				
			}
			if (sumx<target.x) {
				
				if (sumx + prefix[num-1].x - prefix[index-1].x < target.x) {
					//System.out.println(sumx + " " + sumy + " num: " + sizeofyes + "stopped by sumx<");
					//return;
				}
				
			}
			if (sumy>target.y) {
				
				if (sumy + prefix[num-1].y - prefix[index-1].y > target.y) {
					//System.out.println(sumx + " " + sumy + " num: " + sizeofyes + "stopped by sumy>");
					//return;
				}
				
			}
			if (sumy<target.y) {
				
				if (sumy + prefix[num-1].y - prefix[index-1].y < target.y) {
					//System.out.println(sumx + " " + sumy + " num: " + sizeofyes + "stopped by sumy<");
					//return;
				}
				
			}
		}
		*/
		
		recursion(sumx, sumy, index+1, sizeofyes, num);
		sumx += array[index].x;
		sumy += array[index].y;
		recursion(sumx, sumy, index+1, sizeofyes+1, num);
	}
		
}
