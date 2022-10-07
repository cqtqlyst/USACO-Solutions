import java.util.*;

public class DNA_Assembly {
	
	static String recursion(String cur, boolean[] visited, int add, int size, String[] strings) {
		visited[add]=true;
		String s=strings[add];
		int indexend=0;
		for (int i=0;i<=s.length();i++) {
			if (cur.indexOf(s.substring(0, i), cur.length()-i)!=-1) {
				indexend=i;
			}
			
		}
		if (indexend==0) {
		}
		else {
			s = s.replace(s.substring(0, indexend), "");
		}
		cur+=s;
		for (int i=0;i<size;i++) {
			if (visited[i]==false) {
				cur = recursion(cur, visited, i, size, strings);
				return cur;
			}
		}
		return cur;
	}

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		String[] array=new String[n];
		for (int i=0;i<n;i++) {
			array[i]=scan.next();
		}
		boolean[] bool=new boolean[n];
		String str;
		int len;
		int min = 5000;
		for (int i=0;i<n;i++) {
			str = recursion("", bool, i, n, array);
			for (int j=0;j<n;j++) {
				bool[j]=false;
			}
			System.out.println(str);
			len = str.length();
			min = Math.min(len, min);
		}
		System.out.println(min);
		scan.close();
	}
	
}
