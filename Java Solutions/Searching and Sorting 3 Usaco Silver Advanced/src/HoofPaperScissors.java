import java.util.*;
public class HoofPaperScissors {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		char[] array=new char[n+1];
		int[] p=new int[n+1];
		int[] s=new int[n+1];
		int[] h=new int[n+1];
		for (int i=1;i<=n;i++) {
			array[i]=scan.next().charAt(0);
			p[i]=p[i-1];
			s[i]=s[i-1];
			h[i]=h[i-1];
			if (array[i]=='P') {
				p[i]=p[i]+1;
			}
			if (array[i]=='S') {
				s[i]=s[i]+1;
			}
			if (array[i]=='H') {
				h[i]=h[i]+1;
			}
		}
		int sum;
		int max=0;
		for (int i=0;i<=n;i++) {
			for (int j=1;j<=3;j++) {
				for (int k=1;k<=3;k++) {
					sum=0;
					if (k!=j) {
						if (j==1 && k==2) {
							sum=h[i]+(p[n]-p[i]);
						}
						if (j==1 && k==3) {
							sum=h[i]+(s[n]-s[i]);
						}
						if (j==2 && k==1) {
							sum=p[i]+(h[n]-h[i]);
						}
						if (j==2 && k==3) {
							sum=p[i]+(s[n]-s[i]);
						}
						if (j==3 && k==1) {
							sum=s[i]+(h[n]-h[i]);
						}
						if (j==3 && k==2) {
							sum=s[i]+(p[n]-p[i]);
						}
						if (sum>max) {
							max=sum;
						}
					}
				}
			}
		}
		System.out.println(max);
		scan.close();
	}

}
