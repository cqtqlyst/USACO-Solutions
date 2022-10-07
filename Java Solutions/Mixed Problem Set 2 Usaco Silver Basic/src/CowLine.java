import java.util.*;

public class CowLine {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		Deque deque=new LinkedList();
		int n=scan.nextInt();
		char c1;
		char c2;
		int current=1;
		Integer in;
		int hi;
		for (int i=0;i<=n;i++) {
			in=new Integer(current);
			c1=scan.next().charAt(0);
			c2=scan.next().charAt(0);
			if (c1=='A') {
				current++;
				if (c2=='L') {
					deque.addFirst(in);
				} else {
					deque.addLast(in);
				}
			} else {
				hi=scan.nextInt();
				for (int j=0;j<hi;j++) {
					if (c2=='L') {
						deque.removeFirst();
					} else {
						deque.removeLast();
					}
				}
			}
		}
		for (int i=0;i<deque.size();i++) {
			System.out.println(deque.peekFirst());
			deque.removeFirst();
		}
	} 
}
