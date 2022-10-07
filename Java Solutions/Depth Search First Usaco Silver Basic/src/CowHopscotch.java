
import java.util.*;
public class CowHopscotch {
	
	public static int dfs(int a, int b, int r, int c, char[][] matrix) {
		if (a==r-1 && b==c-1) {
			return 1;
		}
		int sum=0;
		for (int i=a+1;i<r;i++) {
			for (int j=b+1;j<c;j++) {
				if (matrix[a][b] != matrix[i][j]) {
					sum+=dfs(i,j,r,c,matrix);
				}
			}
		}
		return sum;
	}
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int r=scan.nextInt();
		int c=scan.nextInt();
		char[][] matrix=new char[r][c];
		String str;
		for (int i=0;i<r;i++) {
			str=scan.next();
			for (int j=0;j<c;j++) {
				matrix[i][j]=str.charAt(j);
			}
		}
		System.out.println(dfs(0,0,r,c,matrix));
	}
}
