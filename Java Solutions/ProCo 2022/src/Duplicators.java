import java.util.*;


public class Duplicators {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int r = scan.nextInt();
		int d = scan.nextInt();
		ArrayList<Character> list = new ArrayList<Character>();
		boolean check = false;
		while (d>0 && r>0) {
			if (r>d) {
				list.add('D');
				r-=d;
			}
			else if (d>r) {
				list.add('R');
				d-=r;
			}
			if ((d==r && d!=1)) {
				System.out.println("IMPOSSIBLE");
				check = true;
				break;
			}
			else if (d == 1 && r == 1) {
				System.out.println("POSSIBLE");
				break;
			}
		}
		if (!check) {
			for (int i = list.size()-1; i>-1; i--) {
				System.out.println(list.get(i));
			}
		}
	}
}
