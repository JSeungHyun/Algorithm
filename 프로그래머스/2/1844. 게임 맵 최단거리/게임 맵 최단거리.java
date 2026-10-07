import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int[][] maps) {
        int h = maps.length;
        int w = maps[0].length;
        
        boolean[][] visited = new boolean[h][w];
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        Deque<Node> dq = new ArrayDeque<>();
        dq.addLast(new Node(0, 0, 1));
        visited[0][0] = true;
        
        while (!dq.isEmpty()) {
            Node node = dq.pollFirst();
            
            if (node.y == h - 1 && node.x == w - 1) {
                return node.v;
            }
            
            for (int i = 0; i < 4; i++) {
                int ny = node.y + dy[i];
                int nx = node.x + dx[i];
                
                if (ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                if (maps[ny][nx] != 1 || visited[ny][nx]) continue;
                
                visited[ny][nx] = true;
                dq.addLast(new Node(ny, nx, node.v + 1));
            }
        }
        
        return -1;
    }
    
    static class Node {
        int y, x, v;
        
        Node(int y, int x, int v) {
            this.y = y;
            this.x = x;
            this.v = v;
        }
    }
}