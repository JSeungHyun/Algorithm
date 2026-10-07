import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = Integer.MAX_VALUE;
        int h = maps.length;
        int w = maps[0].length;
        boolean[][] visitied = new boolean[h][w];
        int[] dy = new int[]{-1, 1, 0, 0};
        int[] dx = new int[]{0, 0, -1, 1};
        Deque<Node> dq = new ArrayDeque<>();
        dq.add(new Node(0, 0, 1));
        visitied[0][0] = true;
        
        while (!dq.isEmpty()) {
            Node node = dq.pollFirst();
            if (node.y == h - 1 && node.x == w - 1) {
                answer = Math.min(answer, node.v);
                continue;
            }
            
            for (int i=0; i<4; i++) {
                int ny = node.y + dy[i];
                int nx = node.x + dx[i];
                
                if (ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                if (maps[ny][nx] != 1 || visitied[ny][nx]) continue;
                if (!(ny == h - 1 && nx == w - 1)) visitied[ny][nx] = true;
                dq.addLast(new Node(ny, nx, node.v + 1));
            }
        }
        
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
    
    public class Node {
        int y;
        int x;
        int v;
        
        public Node(int y, int x, int v) {
            this.y = y;
            this.x = x;
            this.v = v;
        }
    }
}