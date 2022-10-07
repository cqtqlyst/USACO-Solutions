import java.util.*;

public class Rectangular_Pasture {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int ans=(int) Math.pow(2, n);
		int subract;
		int[] x=new int[n];
		int[] y=new int[n];
		for (int i=0;i<n;i++) {
			x[i]=scan.nextInt();
			y[i]=scan.nextInt();
		}
		for (int i=0;i<n-2;i++) {
			for (int j=i+1;j<n-1;j++) {
				for (int k=j+1;k<n;k++) {
					if (x[i]<x[j] && x[j]<x[k] && y[i]<y[j] && y[j]<y[k]) {
						subract=(int) Math.pow(2, n-3);
						ans=ans-subract;
					}
					else if (x[i]>x[j] && x[j]>x[k] && y[i]>y[j] && y[j]>y[k]) {
						subract=(int) Math.pow(2, n-3);
						ans=ans-subract;
					}
				}
			}
		}
		System.out.println(ans);
		scan.close();
	}

}
