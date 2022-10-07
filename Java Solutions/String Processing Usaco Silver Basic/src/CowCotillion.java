import java.util.*;
public class CowCotillion {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int length;
		String str;
		int bal=0;
		int a=0;
		for (int i=0;i<n;i++) {
			length=scan.nextInt();
			str=scan.next();
			for (int j=0;j<length;j++) {
				if (str.charAt(j)=='>') {
					bal++;
				} else {
					bal--;
				}
				if (bal<0) {
					a=1;
				}
			}
			if (a==1 || bal!=0) {
				System.out.println("illegal");
			} else {
				System.out.println("legal");
			}
			bal=0;
			a=0;
		}
		
	}
}