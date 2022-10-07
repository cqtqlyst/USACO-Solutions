import java.io.*;
import java.util.*;
public class Rental_Service {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("rental.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("rental.out")));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int[] milkProduced = new int[n];
		for(int i = 0; i < n; i++) {
			milkProduced[i] = Integer.parseInt(br.readLine());
		}
		sort(milkProduced);
		Shop[] shops = new Shop[m];
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			shops[i] = new Shop(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		}
		Arrays.sort(shops);
		long[] maxProfit = new long[n+1];
		{
			int index = 0;
			for(int i = 0; i < n; i++) {
				maxProfit[i+1] = maxProfit[i];
				while(index < m && milkProduced[i] > 0) {
					int use = Math.min(milkProduced[i], shops[index].quantity);
					maxProfit[i+1] += use * (long)shops[index].price;
					milkProduced[i] -= use;
					shops[index].quantity -= use;
					if(shops[index].quantity == 0) {
						index++;
					}
				}
			}
		}
		int[] rental = new int[r];
		for(int i = 0; i < r; i++) {
			rental[i] = Integer.parseInt(br.readLine());
		}
		sort(rental);
		{
			int a = n-1;
			int rI = 0;
			long rentalSoFar = 0;
			while(a >= 0 && rI < r) {
				rentalSoFar += rental[rI];
				maxProfit[a] += rentalSoFar;
				rI++;
				a--;
			}
		}
		long ret = 0;
		for(long out: maxProfit) {
			ret = Math.max(ret, out);
		}
		pw.println(ret);
		pw.close();
	}

	public static void sort(int[] l) {
		Arrays.sort(l);
		for(int i = 0; i < l.length-1-i; i++) {
			l[i] ^= l[l.length-1-i];
			l[l.length-1-i] ^= l[i];
			l[i] ^= l[l.length-1-i];
		}
	}

	static class Shop implements Comparable<Shop> {
		public int quantity, price;
		public Shop(int a, int b) {
			quantity=a;
			price=b;
		}
		public int compareTo(Shop s) {
			return s.price - price;
		}
	}

}

/*
import java.util.*;
import java.io.*;

public class Rental_Service {
	static class Store {
		int gallon;
		int price;
	}
	static class rents {
		int n;
	}
	static class Comp implements Comparator<Store> {
		public int compare (Store one, Store two) {
			return Integer.compare(one.price, two.price);
		}
	}
	static class Comp2 implements Comparator<rents> {
		public int compare(rents one, rents two) {
			if (one.n<two.n) {
				return 1;
			}
			if (two.n<one.n) {
				return -1;
			}
			return 0;
		}
	}
	public static void main(String[] args) throws IOException {
		Scanner scan = new Scanner(new File("rental.in"));
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("rental.out")));
		int n = scan.nextInt();
		int m = scan.nextInt();
		int r = scan.nextInt();
		int[] cows = new int[n]; //the amount of each milk each cow produces
		Store[] stores = new Store[m]; //the stores that has gallons and price
		rents[] rent = new rents[r]; //the values of the rent
		for (int i = 0; i<n; i++) {
			cows[i] = scan.nextInt();
		}
		for (int i = 0; i<m; i++) {
			stores[i] = new Store();
			stores[i].gallon = scan.nextInt();
			stores[i].price = scan.nextInt();
		}
		for (int i = 0; i<r; i++) {
			rent[i] = new rents();
			rent[i].n = scan.nextInt();
		}
		//sorting
		Arrays.sort(rent, new Comp2());
		Arrays.sort(cows);
		Arrays.sort(stores, new Comp());
		int index = 0;
		long[] maxProfit = new long[n+1];
		for(int i = 0; i < n; i++) {
			maxProfit[i+1] = maxProfit[i];
			while(index < m && cows[i] > 0) {
				int use = Math.min(cows[i], stores[index].gallon);
				maxProfit[i+1] += use * (long)stores[index].price;
				cows[i] -= use;
				stores[index].gallon -= use;
				if(stores[index].gallon == 0) {
					index++;
				}
			}
		}
		for (int i = 0; i<r; i++) {
			System.out.println(rent[i].n);
		}
		int a = n-1;
		int rI = 0;
		long rentalSoFar = 0;
		while(a >= 0 && rI < r) {
			rentalSoFar += rent[rI].n;
			maxProfit[a] += rentalSoFar;
			rI++;
			a--;
		}
		long fn = 0;
		long ret = 0;
		for (int i = 0; i<n; i++) {
			fn = maxProfit[i];
			ret = Math.max(fn, ret);
		}
		System.out.println(Arrays.toString(maxProfit));
		out.println(ret);
		scan.close();
		out.close();
	}
}
*/
