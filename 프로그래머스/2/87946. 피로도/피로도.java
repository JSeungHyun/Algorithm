import java.util.*;

class Solution {
    static int answer = 0;
    static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        search(k, 0, dungeons);
        return answer;
    }
    
    public void search(int hp, int v, int[][] dungeons) {
        answer = Math.max(answer, v);
        
        for (int i=0; i<dungeons.length; i++) {
            if (!visited[i]) {
                if (hp - dungeons[i][0] >= 0) {
                    visited[i] = true;
                    search(hp - dungeons[i][1], v + 1, dungeons);
                    visited[i] = false;
                }
            }
        }
    }
}