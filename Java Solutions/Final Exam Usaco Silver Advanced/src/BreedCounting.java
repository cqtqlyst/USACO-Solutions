import java.util.*;

public class BreedCounting {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int q=scan.nextInt();
		int[] h=new int[n+1];
		int[] g=new int[n+1];
		int[] j=new int[n+1];
		h[0]=0;
		g[0]=0;
		j[0]=0;
		int num;
		for (int i=1;i<=n;i++) {
			num=scan.nextInt();
			j[i]=j[i-1];
			h[i]=h[i-1];
			g[i]=g[i-1];
			if (num==1){
				h[i]++;
			}
			if (num==2){
				g[i]++;
			}
			if (num==3) {
				j[i]++;
			}
		}
		int start;
		int end;
		for (int i=1;i<=q;i++) {
			start=scan.nextInt();
			end=scan.nextInt();
			System.out.print(h[end]-h[start-1]+" ");
			System.out.print(g[end]-g[start-1]+" ");
			System.out.print(j[end]-j[start-1]+" ");
			System.out.println();
		}
		scan.close();
	}
}
