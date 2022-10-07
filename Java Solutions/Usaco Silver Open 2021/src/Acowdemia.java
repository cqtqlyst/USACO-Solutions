import java.util.*;

public class Acowdemia {
	
	static void bs(int[] arr, int find) {
		int max=arr.length;
		int min=0;
		int mid;
		while (max>=min) {
			mid=(max+min)/2;
			
		}
	}

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int k=scan.nextInt();
		int l=scan.nextInt();
		int[] array=new int[n];
		int[] arrs=new int[n];
		for (int i=0;i<n;i++) {
			array[i]=scan.nextInt();
		}
		Arrays.sort(array);
		bs(array, 5);
		scan.close();
		
	}
	
}
