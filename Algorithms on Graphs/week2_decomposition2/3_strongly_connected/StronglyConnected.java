import java.util.*;

public class StronglyConnected {
    private static int numberOfStronglyConnectedComponents(ArrayList<Integer>[] adj) {
        //write your code here
        Stack<Integer> stack = new Stack<Integer>();          // used stack for store order of postvisit
        int visited[] = new int[adj.length];                  // keep track of visited nodes
        Arrays.fill(visited, 0);

        for(int i=0; i < adj.length; i++)                     // travese through all nodes
        {
            if(visited[i] == 0)                               // if node visited
            {
                dfs(visited, adj, i, stack);                  // start dfs from that node
            }
        }

        Arrays.fill(visited, 0);                          // reset visited array which keep track of visited nodes

        int SCC = 0;                                          // strongly connected components
        ArrayList<Integer>[] reverseAdj = reverseGraph(adj);  // reverse the graph by (revesering adjacency list)

        while(!stack.isEmpty())                               // traverse through node according to PostVisit order of nodes
        {
            int currNode = stack.pop();                       // take node at the top
            if(visited[currNode] == 0)
            {
                reverseDfs(visited, reverseAdj, currNode);    // reverse DFS
                SCC++;                                        // add 1 to total number of Stringly Connected Componenets
            }
        }

        return SCC;
    }

    public static  void dfs(int[] visited, ArrayList<Integer>[] adj, int x, Stack<Integer> stack)
    {
        visited[x] = 1;

        for(int i: adj[x])
        {
            if(visited[i] == 0)
            {
                dfs(visited, adj, i, stack);
            }
        }
        stack.push(x);                               // add nodes according to their PostVisit Order
    }

    public static ArrayList<Integer>[] reverseGraph(ArrayList<Integer>[] adj)
    {
        ArrayList<Integer>[] reverseAdj = new ArrayList[adj.length];

        for(int i=0; i < adj.length; i++)
        {
            reverseAdj[i] = new ArrayList<Integer>();           // create arraylist of adajcent nodes for every node
        }

        for(int i=0; i < adj.length; i++)
        {
            for(int j=0; j < adj[i].size(); j++)
            {
                reverseAdj[adj[i].get(j)].add(i);              // reverse edge
            }
        }
        return reverseAdj;
    }

    public static  void reverseDfs(int[] visited, ArrayList<Integer>[] reverseAdj, int x)
    {
        visited[x] = 1;

        for(int i: reverseAdj[x])
        {
            if(visited[i] == 0)
            {
                reverseDfs(visited, reverseAdj, i);
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
        }
        System.out.println(numberOfStronglyConnectedComponents(adj));
    }
}

