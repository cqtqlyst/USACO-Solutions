import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.*;

public class Subset_Equality {
	static class c {
		char letter;
		int index;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
		Scanner scan = new Scanner(System.in);
		String s = st.nextToken();
		st = new StringTokenizer(input.readLine());
		String t = st.nextToken();
		String query;
		st = new StringTokenizer(input.readLine());
		int q = Integer.parseInt(st.nextToken());
		String[] dict = new String[18];
		//bruh
		dict[0] = "a";
		dict[1] = "b";
		dict[2] = "c";
		dict[3] = "d";
		dict[4] = "e";
		dict[5] = "f";
		dict[6] = "g";
		dict[7] = "h";
		dict[8] = "i";
		dict[9] = "j";
		dict[10] = "k";
		dict[11] = "l";
		dict[12] = "m";
		dict[13] = "n";
		dict[14] = "o";
		dict[15] = "p";
		dict[16] = "q";
		dict[17] = "r";
		//done with bruh
		for (int i = 0; i<q; i++) {
			st = new StringTokenizer(input.readLine());
			query = st.nextToken();
			String copys = s;
			String copyt = t;
			boolean[] marked = new boolean[18];
			for (int j = 0; j<query.length(); j++) {
				marked[query.charAt(j) - 'a'] = true;
			}
			for (int j = 0; j<18; j++) {
				if (marked[j] == false) {
					copys = copys.replaceAll(dict[j], "");
					copyt = copyt.replaceAll(dict[j], "");
				}
			}
			if (copys.compareTo(copyt) != 0) {
				System.out.print("N");
				
			}
			else {
				System.out.print("Y");
			}
		}
	}
}
/*
ArrayList<Integer>[] sarr = new ArrayList[18];
ArrayList<Integer>[] tarr = new ArrayList[18];
for (int i = 0; i<18; i++) {
	sarr[i] = new ArrayList<Integer>();
	tarr[i] = new ArrayList<Integer>();
}
for (int i = 0; i<s.length(); i++) {
	sarr[s.charAt(i) - 'a'].add(i);
}
for (int i = 0; i<t.length(); i ++) {
	tarr[t.charAt(i) - 'a'].add(i);
}
for (int i = 0; i<q; i++) {
	ArrayList<c> arr = new ArrayList<c>();
	query = scan.next();
	for (int j = 0; j<query.length(); j++) {
		
	}
}
*/
