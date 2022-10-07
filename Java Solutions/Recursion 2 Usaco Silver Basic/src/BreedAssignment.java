import java.util.*;

public class BreedAssignment {
	public static int countpos(int x,int[][] arr,int[] curval,int n) {
	    int counter=0;
		if (x==n) {
			return 1;
		}
		for (int c=1;c<=3;c++) {
			boolean ok=true;
			for (int i=0;i<x;i++) {
				if (arr[i][x]==1 && curval[i]!=c) {
					ok=false;
				}
				if (arr[i][x]==2 && curval[i]==c) {
					ok=false;
				}
			}
			if (ok==true) {
				curval[x]=c;
				counter+=countpos(x+1, arr, curval, n);
			}
		}
		return counter;
	} 
	
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int k=scan.nextInt();
		int[] curval=new int[n];
		int[][] arr=new int[n][n];
		char c;
		int first;
		int second;
		int a;
		for (int i=0;i<n;i++) {
			curval[i]=0;
		}
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				arr[i][j]=0;
			}
		}
		for (int i=0;i<k;i++) {
			c=scan.next().charAt(0);
			first=scan.nextInt();
			second=scan.nextInt();
			if (c=='S') {
				a=1;
			} else {
				a=2;
			}
			arr[first-1][second-1]=a;
			arr[second-1][first-1]=a;
		}
		
		System.out.println(countpos(0, arr, curval, n));
		
	}
	
}