import java.util.*;

public class The_Big_Dance {
	
	static int recursion(ArrayList list, int sum) {
		ArrayList<Integer> newlist1 = new ArrayList<Integer>();
		ArrayList<Integer> newlist2 = new ArrayList<Integer>();
		int b;
		Integer a;
		if (list.size()==1) {
			return 0;
		}
		else if (list.size()==2) {
			sum += list.get(0) * list.get(1);
			return sum;
		}
		for (int i=0;i<(list.size()+1)/2;i++) {
			b=list.get(i);
			a = new Integer(b);
			newlist1.add(a);
		}
		for (int i=(list.size()+1)/2;i<list.size();i++) {
			b=list.get(i);
			a = new Integer(b);
			newlist2.add(a);
		}
		if (list.size>2) {
			sum += recursion(newlist1, sum);
			sum += recursion(newlist2, sum);	
		}
		return sum;
		
	}

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		ArrayList<Integer> array = new ArrayList<Integer>();
		Integer j;
		for (int i=1;i<=n;i++) {
			j = new Integer(i);
			array.add(j);
		}
		
	}
}
