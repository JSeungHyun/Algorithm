import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] wire : wires) {
            List<Integer> startArr = map.getOrDefault(wire[0], new ArrayList<>());
            startArr.add(wire[1]);
            map.put(wire[0], startArr);
            
            List<Integer> endArr = map.getOrDefault(wire[1], new ArrayList<>());
            endArr.add(wire[0]);
            map.put(wire[1], endArr);
        }
        
        for (int i=0; i<n-1; i++) {
            boolean[] visited = new boolean[n + 1];
            Deque<Integer> dq = new ArrayDeque<>();
            dq.addLast(1);
            visited[1] = true;
            int[] skip = wires[i];
            
            while (!dq.isEmpty()) {
                int s = dq.pollFirst();
                List<Integer> targetList = map.getOrDefault(s, new ArrayList<>());
                for (int target : targetList) {
                    if (visited[target]) continue;
                    if ((s == skip[0] && target == skip[1]) || 
                        (s == skip[1] && target == skip[0])) continue;
                    visited[target] = true;
                    dq.addLast(target);
                }
            }
            
            int cnt = 0;
            for (boolean flag : visited) if (flag) cnt++;
            answer = Math.min(answer, Math.abs((n - cnt) - cnt));
        }
        
        return answer;
    }
}