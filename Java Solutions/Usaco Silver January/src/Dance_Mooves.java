import java.util.*;

public class Dance_Mooves {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int k=scan.nextInt();
		int[] swap1=new int[k];
		int[] swap2=new int[k];
		for (int i=0;i<k;i++) {
			swap1[i]=scan.nextInt();
			swap2[i]=scan.nextInt();
		}
		/*
		for (int i=0;i<k;i++) {
			System.out.println(swap1[i] + ", " + swap2[i]);
		}
		*/
		int[] array=new int[n+1];
		int[][] matrix=new int[n+1][n+1];
		for (int i=1;i<=n;i++) {
			array[i]=i;
		}
		for (int i=0;i<n+1;i++) {
			for (int j=0;j<n+1;j++) {
				matrix[i][j]=0;
			}
		}
		int swap;
		int x=0;
		while (true) {
			for (int i=0;i<k;i++) {
				swap=array[swap1[i]];
				array[swap1[i]]=array[swap2[i]];
				array[swap2[i]]=swap;
				matrix[array[swap2[i]]][i]=1;
				matrix[array[swap1[i]]][i]=1;
			}
			for (int i=1;i<n+1;i++) {
				if (array[i]!=i) {
					x=1;
				}
			}
			if (x==0) {
				break;
			}
			x=0;
		}
		int sum=0;
		for (int i=1;i<n+1;i++) {
			for (int j=1;j<n+1;j++) {
				if (matrix[i][j]==1) {
					sum++;
				}
			}
			System.out.println(sum+1);
			sum=0;
		}
		scan.close();
	}
}
