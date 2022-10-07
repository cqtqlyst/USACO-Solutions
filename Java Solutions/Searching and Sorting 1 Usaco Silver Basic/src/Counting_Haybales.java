import java.util.*;

public class Counting_Haybales {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int q=scan.nextInt();
		int[] arr=new int[n+1];
		for (int i=1;i<=n;i++) {
			arr[i]=scan.nextInt();
		}
		Arrays.sort(arr);
		
		
		scan.close();
		
	}
	
}
