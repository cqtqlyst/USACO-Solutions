import java.util.*;

public class Just_Green_Enough {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int[][] m=new int[n][n];
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				m[i][j]=scan.nextInt();
			}
		}
		long sum=0;
		boolean found=false;
		boolean yes=true;
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				for (int k=i;k<n;k++) {
					for (int l=j;l<n;l++) {
						found=false;
						for (int a=i;a<=k;a++) {
							if (yes==false) {
								break;
							}
							for (int b=j;b<=l;b++) {
								if (m[a][b]<100) {
									yes=false;
									break;
								}
								if (m[a][b]==100) {
									found=true;
								}
							}
						}
						if (yes==true && found==true) {
							sum++;
						}
						yes=true;
						found=false;
					}
				}
			}
		}
		System.out.println(sum);
		scan.close();
	}
	
}
