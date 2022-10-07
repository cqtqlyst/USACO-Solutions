import java.util.*;

public class BuyOneGetOneFree {

	static class struct {
		int size;
		boolean hl;
	}
	static class comp implements Comparator <struct> { 
		public int compare(struct c1, struct c2) {
			if (c1.size<c2.size) {
				return -1;
			}
			if (c2.size<c1.size) {
				return 1;
			}
			if (c2.size==c1.size && c1.hl==false) {
				return -1;
			}
			else {
				return 1;
			}
		}
	}
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int m=scan.nextInt();
		int[] hiqual=new int[n];
		int[] lowqual=new int[m];
		for (int i=0;i<n;i++) {
			hiqual[i]=scan.nextInt();
		}
		for (int i=0;i<m;i++) {
			lowqual[i]=scan.nextInt();
		}
		Arrays.sort(hiqual);
		Arrays.sort(lowqual);
		struct[] array=new struct[n+m];
		for (int i=0;i<n;i++) {
			array[i]=new struct();
			array[i].size=hiqual[i];
			array[i].hl=false;
		}
		int counter=0;
		for (int i=n;i<n+m;i++) {
		    array[i]=new struct();
			array[i].size=lowqual[counter];
			counter++;
			array[i].hl=true;
		}
		Arrays.sort(array,new comp());
		counter=0;
		int ans=0;
		for (int i=0;i<n+m;i++) {
			if (array[i].hl==true) {
				counter++;
			} else {
				if (counter>0) {
					ans++;
					counter--;
				}
			}
		}
		ans+=n;
		System.out.println(ans);
		scan.close();
	}
}
