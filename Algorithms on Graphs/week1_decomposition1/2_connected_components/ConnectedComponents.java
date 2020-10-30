import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class ConnectedComponents {
    private static int numberOfComponents(ArrayList<Integer>[] adj) {
        int cc = 0;
        //write your code here
        int visited[] = new int[adj.length];        // make array to keep track of visited nodes
        Arrays.fill(visited, 0);                // initially set all values to 0

        for(int i=0; i < adj.length; i++)           // iterate trough all nodes
        {
            if(visited[i] == 0)                     // if node is note visited
            {
                explore(visited, adj, i);           // explore from that node
                cc++;                               // add 1 to connected Componnet count
            }
        }

        return cc;
    }

    public static  void explore(int[] visited, ArrayList<Integer>[] adj, int x)    // function to explore DFS from specific node
    {
        visited[x] = 1;                            // make node as visited

        for(int i: adj[x])                         // iterate through all adjacent nodes
        {
            if(visited[i] == 0)                    // if not visited
            {
                explore(visited, adj, i);          // explore from that node
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
        System.out.println(numberOfComponents(adj));
    }
}

