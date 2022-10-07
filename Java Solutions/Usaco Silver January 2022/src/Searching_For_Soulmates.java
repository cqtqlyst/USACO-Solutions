import java.util.*;

public class Searching_For_Soulmates {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		long a;
		long b;
		for (int i = 0; i<n; i++) {
			a = scan.nextLong();
			b = scan.nextLong();
			long count = 0;
			if (a>b) {
				while (a!=b) {
					if (a%2 == 1) {
						a++;
						count++;
					}
					if (a > b) {
						a/=2;
						count++;
					}
					if (a < b) {
						break;
					}
				}
				
			}
			else if (a<b) {
				count = recursion(a, b, count);
			}
			count = recursion(a, b, count);
			System.out.println(count);
		}
	}
	public static long recursion(long n1, long n2, long count) {
		count++;
		if (n1+1 == n2 || n1*2 == n2) {
			return count;
		}
		if (n1*2 > n2) {
			return recursion(n1+1, n2, count);
		}
		return Math.min(recursion(n1+1, n2, count), recursion(n1*2, n2, count));
		
		
	}
	/*
	if (a>b) {
		while (a!=b) {
			if (a%2 == 1) {
				a++;
				count++;
			}
			if (a > b) {
				a/=2;
				count++;
			}
			if (a < b) {
				break;
			}
		}
		
	}
	else if (a<b) {
		count = recursion1(a, b, count);
	}
	*/
}
