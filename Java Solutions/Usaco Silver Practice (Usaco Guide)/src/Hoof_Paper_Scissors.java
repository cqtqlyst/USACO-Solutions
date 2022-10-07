import java.util.*;
import java.io.*;

public class Hoof_Paper_Scissors {
	public static class Struct {
		int hoof;
		int paper;
		int scissors;
	}
	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(new File("hps.in"));
		PrintWriter out = new PrintWriter(new File("hps.out"));
		int n = scan.nextInt();
		Struct[] array = new Struct[n+1];
		String s;
		for (int i = 0; i<n+1; i++) {
			array[i] = new Struct();
		}
		array[0].hoof = 0;
		array[0].paper = 0;
		array[0].scissors = 0;
		for (int i = 1; i<n+1; i++) {
			s=scan.next();
			array[i].hoof = array[i-1].hoof;
			array[i].paper = array[i-1].paper;
			array[i].scissors = array[i-1].scissors;
			if (s == "H") {
				array[i].hoof++;
			}
			else if (s == "P") {
				array[i].paper++;
			}
			else {
				array[i].scissors++;
			}
		}
		for (int i = 1; i<n+1; i++) {
			
		}
		scan.close();
		out.close();
	}
}
