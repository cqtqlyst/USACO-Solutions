import java.util.*;

public class Subway_Tunnel {
	
	static ArrayList<Integer>[] adjacencyGraph;
	static boolean[] visited;
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int m = scan.nextInt();
		adjacencyGraph = new ArrayList[n+1];
		visited = new boolean[n+1];
		int a, b;
		for (int i = 1; i<n+1; i++) {
			adjacencyGraph[i] = new ArrayList<Integer>();
		}
		for (int i = 0; i<m; i++) {
			a = scan.nextInt();
			b = scan.nextInt();
			adjacencyGraph[a].add(b);
			adjacencyGraph[b].add(a);			
		}
		dfs(1);
		for (int i = 1; i<n+1; i++) {
			if (visited[i] == false) {
				System.out.println(i);
			}
		}
	}
	
	public static void dfs(int currNode) {
		visited[currNode] = true;
		for (Integer i : adjacencyGraph[currNode]) {
			if (visited[currNode] == false) {
				dfs(adjacencyGraph[currNode].get(i));
			}
		}
		
	}
}
