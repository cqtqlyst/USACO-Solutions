import java.util.*;
import java.io.*;


public class Breed_Counting {
	static class Struct {
		int holstein;
		int guernsey;
		int jersey;
	}
	
	public static void main (String[] args) throws IOException {
		Scanner scan = new Scanner(new File("bcount.in"));
		PrintWriter out = new PrintWriter(new File("bcount.out"));
		int n = scan.nextInt();
		int q = scan.nextInt();
		Struct[] array = new Struct[n+1];
		for (int i = 0; i<n+1; i++) {
			array[i] = new Struct();
		}
		array[0].holstein = 0;
		array[0].guernsey = 0;
		array[0].jersey = 0;
		int cownum;
		for (int i = 1; i<n+1; i++) {
			cownum = scan.nextInt();
			array[i].holstein = array[i-1].holstein;
			array[i].guernsey = array[i-1].guernsey;
			array[i].jersey = array[i-1].jersey;
			if (cownum == 1) {
				array[i].holstein++;
			}
			else if (cownum == 2) {
				array[i].guernsey++;
			}
			else {
				array[i].jersey++;
			}
		}
		int start, end;
		for (int i = 0; i<q; i++) {
			start = scan.nextInt();
			end = scan.nextInt();
			out.println((array[end].holstein - array[start-1].holstein) + " " + (array[end].guernsey - array[start-1].guernsey) + " " + (array[end].jersey - array[start-1].jersey));
		}
		scan.close();
		out.close();
	}
}
