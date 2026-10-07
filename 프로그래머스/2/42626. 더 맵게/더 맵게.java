import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int scov : scoville) pq.add(scov);
        
        while (!pq.isEmpty()) {
            int n1 = pq.poll();
            
            
            if (n1 >= K) return answer;
            if (pq.isEmpty()) return -1;
            
            int n2 = pq.poll();
            pq.add(n1 + (n2 * 2));
            answer++;
        }
        
        return -1;
    }
}