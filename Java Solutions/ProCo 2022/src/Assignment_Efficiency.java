import java.util.*;
import java.io.*;
public class Assignment_Efficiency {
	static class assignment {
		int index;
		double weight;
	}
	
	static class comp implements Comparator<assignment> {
		public int compare(assignment one, assignment two) {
			if (one.weight<two.weight) {
				return -1;
			}
			else if (one.weight>two.weight) {
				return 1;
			}
			else {
				if (one.index>two.index) {
					return -1;
				}
				if (one.index<two.index) {
					return 1;
				}
			}
			return 0;
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
		int n = Integer.parseInt(st.nextToken());;
		assignment[] arr = new assignment[n];
		int ind = 0;
		int points = 0;
		int time = 0;
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(input.readLine());
			arr[i] = new assignment();
			ind = Integer.parseInt(st.nextToken());;
			points = Integer.parseInt(st.nextToken());;
			time = Integer.parseInt(st.nextToken());;
			arr[i].index = ind;
			arr[i].weight = (double) points/time;
		}
		Arrays.sort(arr, new comp());
		for (int i = n-1; i>-1; i--) {
			System.out.println((arr[i].index));
		}
		
	}
}
