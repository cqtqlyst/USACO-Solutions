import java.util.*;

public class Lifeguards {
	static class struct {
		int pos;
		int label;
		int index;
	}
	static class comp implements Comparator <struct> { 
		public int compare(struct c1, struct c2) {//compare function will take two cities
			if (c1.pos<c2.pos)//it will sort the array by population in ascending order 
				return -1;
			else if (c1.pos==c2.pos) {
				if (c1.label>c2.label) {
					return -1;
				}
				return 1;
			}
			return 1;
		}
	}
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		struct[] cows=new struct[2*n];
		for (int i=0;i<n*2;i++) {
			cows[i]=new struct();
		}
		int start;
		int end;
		int total=0;
		for (int i=0;i<n;i++) {
			start=scan.nextInt();
			end=scan.nextInt();
			total+=end-start;
			cows[2*i].pos=start;
			cows[(2*i)+1].pos=end;
			cows[2*i].label=1;
			cows[(2*i)+1].label=-1;
			cows[2*i].index=i;
			cows[(2*i)+1].index=i;
		}
		Arrays.sort(cows,new comp());
		
		scan.close();
	}
	
}
