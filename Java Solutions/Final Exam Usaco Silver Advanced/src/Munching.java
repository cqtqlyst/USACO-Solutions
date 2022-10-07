import java.util.*;
@SuppressWarnings("unchecked") 
public class Munching {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int row=scan.nextInt();
		int col=scan.nextInt();
		char[][] m=new char[row][col];
		Queue<Integer> qrow=new LinkedList<Integer>();
		Queue<Integer> qcol=new LinkedList<Integer>();
		Queue<Integer> qmoves=new LinkedList<Integer>();
		int[] ix=new int[4];
		int[] iy=new int[4];
		iy[0]=1;
		iy[1]=0;
		iy[2]=-1;
		iy[3]=0;
		ix[0]=0;
		ix[1]=1;
		ix[2]=0;
		ix[3]=-1;
		String s;
		int rbarn=0;
		int cbarn=0;
		for (int i=0;i<row;i++) {
			s=scan.next();
			for (int j=0;j<col;j++) {
				m[i][j]=s.charAt(j);
				if (m[i][j]=='B') {
					rbarn=i;
					cbarn=j;
				}
			}
		}
		qrow.add(rstart);
		qcol.add(cstart);
		
		
		scan.close();
	}
}
