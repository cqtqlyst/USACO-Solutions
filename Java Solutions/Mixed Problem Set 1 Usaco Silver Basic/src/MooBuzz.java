import java.util.*;
public class MooBuzz {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		n--;
		int[] x={1,2,4,7,8,11,13,14};
		System.out.println((n/8*15)+x[n%8]);
		
	}
}
