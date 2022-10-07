import java.util.*;

public class TimeCards {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int nlines=scan.nextInt();
		int[] array=new int[n+1];
		int cow;
		String str;
		int hr;
		int min;
		for (int i=0;i<nlines;i++) {
			cow=scan.nextInt();
			str=scan.next();
			hr=scan.nextInt();
			min=scan.nextInt();
			min+=(60*hr);
			if (str.equals("START")) {
				array[cow]-=min;
			} else {
				array[cow]+=min;
			}
		}
		for (int i=1;i<=n;i++) {
			System.out.print(array[i]/60 + " ");
			System.out.println(array[i]%60);
		}
	}
}
