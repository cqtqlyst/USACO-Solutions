import java.util.*;

public class HaybaleStacking {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int q=scan.nextInt();
		int[] array=new int[n];
		int start;
		int end;
		for (int i=0;i<q;i++) {
			start=scan.nextInt();
			end=scan.nextInt();
			for (int j=start;j<end;j++) {
				array[j]++;
			}
		}
		Arrays.sort(array);
		System.out.println(array[(n/2)+1]);
		scan.close();
	}
}
