import java.util.*;
import java.io.*;
public class Palm_Trees {
    
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int[] coords = new int[1000000];
        int last = 0;
        for (int i = 0; i<n; i++) {
            st = new StringTokenizer(input.readLine());
            int index = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());
            coords[index] = value;
            last = index;
        }
        //for (int i = 0; i<last+1; i++) {
        	//System.out.print(coords[i] + " ");
        //}
        //System.out.println();
        int ind = 1;
        int max = 0;
        for (int i = 1; i<last+1; i++) {
            if (coords[i]>h) {
            	//System.out.println(ind + " " + i);
                max = Math.max((i-1) - ind, max);
                ind = i+1;
            }
        }
        System.out.println(max);
    }
}
