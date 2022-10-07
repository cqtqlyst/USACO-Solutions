import java.util.*;
import java.io.*;

public class Static_Range_Sum {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int n = scan.nextInt();
        int q = scan.nextInt();
        long[] a = new long[n];
        for (int i = 0; i<n; i++) {
            a[i] = scan.nextInt();
        }
        long[] prefix = new long[n+1];
        for (int i = 0; i<n; i++) {
            prefix[i+1] = prefix[i] + a[i];
        }
        int l,r;
        for (int i = 0; i<q; i++) {
            l = scan.nextInt();
            r = scan.nextInt();
            out.println(prefix[r] - prefix[l]);
        }
        scan.close();
        out.close();
    }
}

