import java.util.*;

public class Comfortable_Cows {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		boolean[][] m = new boolean[1001][1001];
		int[] x=new int[n];
		int[] y=new int[n];
		for (int i=0;i<n;i++) {
			x[i]=scan.nextInt();
			y[i]=scan.nextInt();
		}
		int ctr=0;
		int totalfornow;
		int notfilledx;
		int notfilledy;
		int[] ix={0, -1, 0, 1};
		int[] iy={1, 0, -1, 0};
		int newnotfilledx;
		int newnotfilledy;
		for (int i=0;i<n;i++) {
			m[x[i]][y[i]]=true;
			totalfornow=0;
			notfilledx=0;
			notfilledy=0;
			for (int j=0;j<i;j++) {
				ctr=0;
				for (int k=0;k<4;k++) {
					if (x[j]+ix[k]<0 || x[j]+ix[k]>1000 || y[j]+iy[k]<0 || y[j]+iy[k]>1000) {
						
					}
					else if (m[x[j]+ix[k]][y[j]+iy[k]]==true) {
						ctr++;
					}
					else if (m[x[j]+ix[k]][y[j]+iy[k]]==false) {
						notfilledx=x[j]+ix[k];
						notfilledy=y[j]+iy[k];
					}
				}
				if (ctr==3) {
					totalfornow++;
					newnotfilledx=0;
					newnotfilledy=0;
					while (true) {
						ctr=0;
						for (int k=0;k<4;k++) {
							if (notfilledx+ix[k]<0 || notfilledx+ix[k]>1000 || notfilledy+iy[k]<0 || notfilledy+iy[k]>1000) {
								
							}
							else if (m[notfilledx+ix[k]][notfilledy+iy[k]]==true) {
								ctr++;
							}
							else if (m[notfilledx+ix[k]][notfilledy+iy[k]]==false) {
								newnotfilledx=notfilledx+ix[k];
								newnotfilledy=notfilledy+iy[k];
							}
						}
						if (ctr==3) {
							totalfornow++;
							notfilledx=newnotfilledx;
							notfilledy=newnotfilledy;
						}
						else {
							break;
						}
					}
				}
			}
			System.out.println(totalfornow);
			
		}
		
		scan.close();
	}
	
}
