import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        Deque<Integer> dq = new ArrayDeque<>();
        
        for (int i=0; i<n; i++) {
            if (visited[i]) continue;
            answer++;
            dq.add(i);
            visited[i] = true;
            
            while (!dq.isEmpty()) {
                int idx = dq.pollFirst();
                for (int j=0; j<n; j++) {
                    if (i == j) continue;
                    if (!visited[j] && computers[idx][j] == 1) {
                        visited[j] = true;
                        dq.addLast(j);
                    }
                }
            }
        }
        
        return answer;
    }
}