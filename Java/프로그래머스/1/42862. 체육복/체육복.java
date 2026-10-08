import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        boolean[] visited = new boolean[n + 1];
        boolean[] res = new boolean[n + 1];
        
        Arrays.fill(visited, true);
        for (int l : lost) visited[l] = false;
        
        for (int r : reserve) {
            if (visited[r]) res[r] = true;
            else visited[r] = true;
        }
        
        System.out.println(Arrays.toString(visited));
        
        for (int i=1; i<=n; i++) {
            if (visited[i]) continue;
            if (res[i-1]) {
                res[i-1] = false;
                visited[i] = true;
            } else if (i != n && res[i+1]) {
                res[i+1] = false;
                visited[i] = true;
            }
        }
        
        int answer = -1;
        for (boolean v : visited) if (v) answer++;
        return answer;
    }
}