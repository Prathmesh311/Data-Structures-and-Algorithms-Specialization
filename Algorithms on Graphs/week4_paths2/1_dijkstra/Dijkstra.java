import java.util.*;

public class Dijkstra {
    public static class Node implements Comparable<Node>
    {
        int index;
        int dist;

        public Node(int index, int dist)
        {
            this.index = index;
            this.dist = dist;
        }

        public int compareTo(Node o)
        {
            if(this.dist > o.dist)
            {
                return 1;
            }
            else if(this.dist < o.dist)
            {
                return -1;
            }
            else {
                return 0;
            }
        }
    }
    private static int distance(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int s, int t) {

        PriorityQueue<Node> pq = new PriorityQueue<Node>();       // priority queue
        int distance[] = new int[adj.length];
        int prev[] = new int[adj.length];
        Arrays.fill(distance, Integer.MAX_VALUE);                 // fill distacne array with inf large value
        Arrays.fill(prev, -1);                                // set all prev value to -1

        pq.add(new Node(s, 0));                               // add source to priority queue
        distance[s] = 0;                                          // set distance of source == 0

        while(!pq.isEmpty())                                      // continue unitl priority queue is not empty
        {
            Node node  = pq.remove();                             // remove min from queue
            int currNode = node.index;
            for(int i: adj[currNode])                             // traverse through all adjacent nodes
            {
                int i_index = adj[currNode].indexOf(i);
                if(distance[i] > distance[currNode] + cost[currNode].get(i_index))  // if dist from currNode is less
                {
                    distance[i] = distance[currNode] + cost[currNode].get(i_index); // set new distance
                    prev[i] = currNode;                                             // mark prev node
                    pq.add(new Node(i, distance[i]));                               // add to priority queue
                }
            }
        }

        if(distance[t] == Integer.MAX_VALUE)       // if node can't be visited return -1
        {
            return -1;
        }
        return distance[t];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[])new ArrayList[n];
        ArrayList<Integer>[] cost = (ArrayList<Integer>[])new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
            cost[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y, w;
            x = scanner.nextInt();
            y = scanner.nextInt();
            w = scanner.nextInt();
            adj[x - 1].add(y - 1);
            cost[x - 1].add(w);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        System.out.println(distance(adj, cost, x, y));
    }
}

