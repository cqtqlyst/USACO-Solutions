import java.util.*;
public class CombinationLock {
	
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int ans=0;
		int[] fj=new int[3];
		int[] master=new int[3];
		for (i=0;i<3;i++) {
			fj[i]=scan.nextInt();
		}
		for (i=0;i<3;i++) {
			master[i]=scan.nextInt();
		}
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				for (int k=1;k<=n;k++) {
					if ((Math.abs(i-fj[0])<=2 || Math.abs(i-fj[0]>=n-2)) &&  (Math.abs(j-fj[1])<=2 || Math.abs(j-fj[1]>=n-2)) && (Math.abs(k-fj[2])<=2 || Math.abs(k-fj[2]>=n-2))) {
						ans++;
					} else if ((Math.abs(i-master[0])<=2 || Math.abs(i-master[0]>=n-2)) &&  (Math.abs(j-master[1])<=2 || Math.abs(j-master[1]>=n-2)) && (Math.abs(k-master[2])<=2 || Math.abs(k-master[2]>=n-2))) {
						ans++;
					}
					
				}
			}
		}
		System.out.println(ans);
	}
}
