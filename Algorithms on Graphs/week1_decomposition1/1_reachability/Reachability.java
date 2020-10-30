import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Reachability {
    private static int reach(ArrayList<Integer>[] adj, int x, int y) {
        //write your code here
        int visited[] = new int[adj.length];          // make array to keep track of visited nodes
        Arrays.fill(visited, 0);                      // initially set all values to 0

        explore(visited, adj, x);                     // start exploring from root node

        return visited[y];                            // return state of destination node if 1 then it's reachable
    }

    public static void explore(int[] visited, ArrayList<Integer>[] adj, int x)    // function to DFS graph
    {
        visited[x] = 1;                               // make node as visited

        for(int i : adj[x])                           // iterate through all adjacent nodes
        {
            if(visited[i] == 0)                       // if not visited
            {
                explore(visited, adj, i);             // visit recursively
            }
        }
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
            adj[y - 1].add(x - 1);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        System.out.println(reach(adj, x, y));
    }
}

