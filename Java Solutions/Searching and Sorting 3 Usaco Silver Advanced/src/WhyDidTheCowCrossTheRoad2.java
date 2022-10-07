import java.util.*;
public class WhyDidTheCowCrossTheRoad2 {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int k=scan.nextInt();
		int b=scan.nextInt();
		int[] broken=new int[b+1];
		for (int i=1;i<=b;i++) {
			broken[i]=scan.nextInt();
		}
		Arrays.sort(broken);
		int[] array=new int[n+1];
		int index=1;
		array[0]=0;
		for (int i=1;i<=n;i++) {
			array[i]=array[i-1];
			if (index<=b) {
				if (i==broken[index]) {
					array[i]=array[i]+1;
					index++;
				}
			}
		}
		int min=1000000;
		for (int i=1;i<=n-k;i++) {
			if (array[i+k]-array[i]<min) {
				min=array[i+k]-array[i];
			}
		}
		System.out.println(min);
		scan.close();
	}

}
