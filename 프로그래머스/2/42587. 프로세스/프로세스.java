import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Deque<Integer> dq = new ArrayDeque<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i=0; i<priorities.length; i++) {
            dq.addLast(i);
            pq.add(priorities[i]);
        }
        
        while (!dq.isEmpty()) {
            int cur = dq.pollFirst();
            
            if (pq.peek() == priorities[cur]) {
                pq.poll();
                answer++;
                
                if (cur == location) return answer;
            } else {
                dq.addLast(cur);
            }
        }
        
        return answer;
    }
}