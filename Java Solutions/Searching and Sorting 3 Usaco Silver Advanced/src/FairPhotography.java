import java.util.*;
public class FairPhotography {
	public static class struct {
		int pos;
		char breed;
	}
	static class comp implements Comparator <struct> { 
		public int compare(struct c1, struct c2) {//compare function will take two positions
			if (c1.pos<c2.pos)//it will sort the array by population in ascending order 
				return -1;
			return 1;
		}
	}
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		struct[] array=new struct[n+1];
		for (int i=1;i<=n;i++) {
			array[i]=new struct();
			array[i].pos=scan.nextInt();
			array[i].breed=scan.next().charAt(0);
		}
		Arrays.sort(array, new comp());
		int[] ps=new int[n+1];
		ps[0]=0;
		for (int i=1;i<=n;i++) {
			if (array[i].breed=='G') {
				ps[i]=ps[i-1]+1;
			}
			else {
				ps[i]=ps[i-1]+1;
			}
		}
		int ans=0;
		int[] ins=new int[(2*n)];
		int[] ine=new int[(2*n)];
		for (int i=0;i<n;i++) {
			if (ins[ps[i]+n]==0) {
				ins[ps[i]+n]=i;
			}
			else {
				ine[ps[i]+n]=i;
			}
			ans=Math.max(ans, array[ine[i]].pos - array[ins[i]].pos);
		}
		System.out.println(ans);
	}
}
