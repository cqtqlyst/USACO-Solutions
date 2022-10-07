import java.util.*;

public class HighCardWins {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		boolean[] cards=new boolean[(2*n)+1];
		int fornow;
		for (int i=1;i<=n;i++) {
			fornow=scan.nextInt();
			cards[fornow]=true;
		}
		int counter=0;
		int ans=0;
		for (int i=1;i<=2*n;i++) {
			if (cards[i]==true) {
				counter++;
			} else {
				if (counter>0) {
					ans++;
					counter--;
				}
			}
		}
		System.out.println(ans);
	}
}
