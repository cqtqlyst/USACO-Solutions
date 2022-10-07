import java.util.*;

public class The_Bovine_Shuffle {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int ans=n;
		int[] v=new int[n];
		int[] freq=new int[n];
		int temp;
		Queue<Integer> q = new LinkedList<Integer>();
		for(int i=0;i<n;i++) {
			v[i]=scan.nextInt();
			v[i]--;
			freq[v[i]]++;
		}
		for (int i=0;i<n;i++) {
			if (freq[i]==0) {
				q.add(i);
				ans--;
			}
		}
		while (q.size()>0) {
			temp=q.remove();
			freq[v[temp]]--;
			if (freq[v[temp]]==0) {
				q.add(v[temp]);
				ans--;
			}
		}
		
		System.out.println(ans);
		scan.close();
	}
}