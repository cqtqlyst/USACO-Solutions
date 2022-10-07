import java.util.*;

public class Ski_Course_Design {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int[] hills=new int[n];
		for (int i=0;i<n;i++) {
			hills[i]=scan.nextInt();
		}
		int mincost=10000000;
		int cost;
		int x=0;
		for (int i=0;i<=83;i++) {
			cost=0;
			for (int j=0;j<n;j++) {
				if (hills[j]<i) {
					x=i-hills[j];
				}
				else if (hills[j]>i+17) {
					x=hills[j]-(i+17);
				}
				else {
					x=0;
				}
				cost+=x*x;
			}
			mincost=Math.min(mincost, cost);
		}
		System.out.println("" + mincost);
		scan.close();

	}

}
