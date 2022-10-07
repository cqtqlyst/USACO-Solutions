import java.util.*;


public class DiningCows {
	
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int[] array=new int[n];
		int rightones=0;
		int lefttwos=0;
		int min=n;
		for (int i=0;i<n;i++) {
			array[i]=scan.nextInt();
			if (array[i]==1) {
				rightones++;
			}
		}
		for (int i=0;i<=n;i++) {
			if (i!=0) {
				if (array[i-1]==2) {
					lefttwos++;
				} else {
					rightones--;
				}
			}
			if (rightones+lefttwos<min) {
				min=rightones+lefttwos;
			}
			
		}
		System.out.println(min);
	} 
	
}
