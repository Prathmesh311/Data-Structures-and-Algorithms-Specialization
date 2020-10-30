import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Acyclicity {
    private static int acyclic(ArrayList<Integer>[] adj) {
        //write your code here
        int isCycle = 0;
        Stack<Integer> stack = new Stack<>();     // stack is used for storing the visited nodes in dfs cycle
        int[] visited = new int[adj.length];
        Arrays.fill(visited, 0);

        for(int i=0; i<adj.length; i++)           // iterate through all nodes
        {
            if(visited[i] == 0)
            {
                isCycle = explore(visited, adj, i, stack);   // explore all nodes from specific node
                if(isCycle == 1)                             // if cycle detected return 1
                {
                    return 1;
                }
            }
        }
        return isCycle;
    }

    public static int explore(int[] visited, ArrayList<Integer>[] adj, int x, Stack<Integer> stack)
    {
        if(stack.contains(x))                      // if node is already in stack then their is cycle in graph
        {
            return 1;                              // return 1 to indiacate (Cycle is detected)
        }

        visited[x] = 1;                            // make node as visited
        stack.push(x);                             // push node in stack

        for(int i: adj[x])
        {
            if(explore(visited,adj,i,stack) == 1)   // if cycle is detected return 1
            {
                return 1;
            }
        }
        stack.pop();                                // pop node from stack
        return 0;
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
        System.out.println(acyclic(adj));
    }
}

