import java.io.*;
import java.util.*;


public class COW_Operations {
	static class cow {
		int c;
		int o;
		int w;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
		String s = st.nextToken();
		st = new StringTokenizer(input.readLine());
		int q = Integer.parseInt(st.nextToken());
		cow[] arr = new cow[s.length()+1];
		arr[0] = new cow();
		arr[0].c = 0;
		arr[0].o = 0;
		arr[0].w = 0;
		for (int i = 1; i<s.length()+1; i++) {
			arr[i] = new cow();
			arr[i].c = arr[i-1].c;
			arr[i].o = arr[i-1].o;
			arr[i].w = arr[i-1].w;
			if (s.charAt(i-1) == 'C') {
				arr[i].c++;
			}
			else if (s.charAt(i-1) == 'O') {
				arr[i].o++;
			}
			else {
				arr[i].w++;
			}
		}
		int start;
		int end;
		int num = 0;
		int diff;
		for (int i = 0; i<q; i++) {
			num = 0;
			st = new StringTokenizer(input.readLine());
			start = Integer.parseInt(st.nextToken());
			end = Integer.parseInt(st.nextToken());
			num += arr[end].c - arr[start-1].c;
			if (arr[end].w - arr[start-1].w < arr[end].o - arr[start-1].o) {
				num += arr[end].w - arr[start-1].w;
				diff = (arr[end].o - arr[start-1].o) - (arr[end].w - arr[start-1].w);
			}
			else {
				num += arr[end].o - arr[start-1].o;
				diff = (arr[end].w - arr[start-1].w) - (arr[end].o - arr[start-1].o);
			}
			if (diff%2 == 0) {
				if (num%2 == 1) {
					System.out.print("Y");
				}
				else {
					System.out.print("N");
				}
			}
			else {
				System.out.print("N");
			}
		}
		
	}
}
