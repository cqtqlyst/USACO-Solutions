import java.util.*;


public class BovineFireDrill {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int[] array=new int[n+1];
		for (int i=1;i<=n;i++) {
			array[i]=i;
		}
		int[] used=new int[n+1];
		for (int i=1;i<=n;i++) {
			used[i]=0;
		}
		int currentloc=1;
		int fornow;
		int numofiters=0;
		while (true) {
			if (used[currentloc]==1 || (currentloc==1 && numofiters!=0)) {
				break;
			}
			used[currentloc]=1;
			fornow=(currentloc*2)%n;
			if (fornow==0) {
				fornow=n;
			}
			array[fornow]=array[currentloc];
			array[currentloc]=0;
			System.out.println(currentloc);
			currentloc=fornow;
			numofiters++;
		}
		System.out.println(currentloc);
	} 
}
