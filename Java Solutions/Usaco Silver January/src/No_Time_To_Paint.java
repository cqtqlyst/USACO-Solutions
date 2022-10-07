import java.util.*;

public class No_Time_To_Paint {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int q=scan.nextInt();
		String s=scan.next();
		int start;
		int end;
		String s1;
		String s2;
		String alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		char first;
		char second;
		int secondpos;
		int x=0;
		int ans1;
		int ans2;
		int ans;
		for (int a=0;a<q;a++) {
			start=scan.nextInt();
			end=scan.nextInt();
			start--;
			end--;
			s1=s.substring(0, start);
			s2=s.substring(end+1, n);
			ans1=s1.length();
			ans2=s2.length();
			if (s1.length()>0) {
				for (int i=0;i<s1.length();i++) {
					first=s1.charAt(i);
					if (s1.indexOf(first, i+1)!=-1) {
						secondpos=s1.indexOf(first, i+1);
						second=s1.charAt(secondpos);
						for (int j=i+1;j<secondpos;j++) {
							if (s1.charAt(j)<first) {
								x=1;
							}
						}
						if (x==0) {
							ans1-=1;
						}
						x=0;
					}
				}
			}
			x=0;
			if (s2.length()>0) {
				for (int i=0;i<s2.length();i++) {
					first=s2.charAt(i);
					if (s2.indexOf(first, i+1)!=-1) {
						secondpos=s2.indexOf(first, i+1);
						second=s2.charAt(secondpos);
						for (int j=i+1;j<secondpos;j++) {
							if (s2.charAt(j)<first) {
								x=1;
							}
						}
						if (x==0) {
							ans2-=1;
						}
						x=0;
					}
				}
			}
			ans=ans2+ans1;
			System.out.println(ans);
		}
		scan.close();
	}
}
