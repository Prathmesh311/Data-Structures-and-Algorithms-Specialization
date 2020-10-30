import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Toposort {
    private static ArrayList<Integer> toposort(ArrayList<Integer>[] adj) {

        int used[] = new int[adj.length];
        ArrayList<Integer> order = new ArrayList<Integer>();        // arraylist for storing order of node visit
        Arrays.fill(used, 0);

        for(int i=0; i < adj.length; i++)                           // DFS
        {
            if(used[i] == 0)
            {
                dfs(adj, used, order, i);
            }
        }
        return order;                                               // return order
    }

    private static void dfs(ArrayList<Integer>[] adj, int[] used, ArrayList<Integer> order, int s) {
      //write your code here
        used[s] = 1;                            // make node as visited

        for (int i: adj[s])                    // iterate through adjacent nodes
        {
            if(used[i] == 0)
            {
                dfs(adj, used, order, i);      // if not visited then explore
            }
        }
        order.add(0, s);                 // add element in order to keep track of order of visiting of node in TopoSort
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[])new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y;
            x = scanner.nextInt();
            y = scanner.nextInt();
            adj[x - 1].add(y - 1);
        }
        ArrayList<Integer> order = toposort(adj);
        for (int x : order) {
            System.out.print((x + 1) + " ");
        }
    }
}

