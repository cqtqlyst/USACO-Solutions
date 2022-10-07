import java.util.*;

public class Sum_of_Three_Values {
	static class array {
		int num;
		int index;
	}
	static class comp implements Comparator<array> {
		public int compare (array one, array two) {
			return (Integer.compare(one.num, two.num));
		}
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		array[] arr = new array[n];
		for (int i = 0; i<n; i++) {
			arr[i] = new array();
			arr[i].num = scan.nextInt();
			arr[i].index = i;
		}
		Arrays.sort(arr, new comp());
		for (int i = 0; i<n; i++) {
			
		}
	}
}
