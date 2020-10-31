import java.lang.reflect.Array;
import java.util.*;

public class Bipartite {
    private static int bipartite(ArrayList<Integer>[] adj) {
        //write your code here
        int colour[]  = new int[adj.length];              // used to colour graph in 2 diff colour
        Arrays.fill(colour, -1);                          // set first all nodes of graph as non-coloured

        for(int i=0; i < adj.length; i++)                 // iterate throgh all nodes
        {
            if(colour[i] == -1)                           // if not coloured
            {
                if(!bfs(colour, adj, i))                  // BFS
                {
                    return 0;
                }
            }
        }
        return 1;
    }

    public static boolean bfs(int[] colour, ArrayList<Integer>[] adj, int x)
    {
        Queue<Integer> q = new LinkedList<>();

        q.add(x);
        colour[x] = 1;

        while(!q.isEmpty())
        {
            int curr = q.remove();
            for(int i: adj[curr])
            {
                if(colour[i] == colour[curr])        // if adjacent nodes are same colour then it's not bipartite graph
                {
                    return false;
                }
                if(colour[i] == -1)                  // if not coloured yet
                {
                    colour[i] = 1 - colour[curr];    // colour adjacent node with diff colour
                    q.add(i);
                }
            }
        }
        return true;

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
        System.out.println(bipartite(adj));
    }
}

