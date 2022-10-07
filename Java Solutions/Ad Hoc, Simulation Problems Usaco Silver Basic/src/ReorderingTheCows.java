import java.util.*;

public class ReorderingTheCows {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int[] a=new int[n+1];
		int[] b=new int[n+1];
		int[] b_inv=new int[n+1];
		for (int i=1;i<n+1;i++) {
			a[i]=scan.nextInt();
		}
		for (int i=1;i<n+1;i++) {
			b[i]=scan.nextInt();
			b_inv[b[i]]=i;
		}
		int numcycles=0;
		int longestcycle=-1;
		int counter;
		int current;
		int next;
		int hi;
		for (int i=1;i<n+1;i++) {
			if (a[i]!=b[i]) {
				numcycles++;
				current=a[i];
				next=b_inv[current];
				counter=0;
				while (next!=i) {
					hi=current;
					current=a[next];
					a[next]=hi;
					next=b_inv[current];
					counter++;
				}
				hi=current;
				current=a[next];
				a[next]=hi;
				counter++;
				longestcycle=Math.max(longestcycle, counter);
			}
		}
		System.out.println(numcycles + " " + longestcycle);
		
	} 
}
