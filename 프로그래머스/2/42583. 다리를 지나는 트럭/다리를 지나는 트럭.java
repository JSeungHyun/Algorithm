import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Deque<Integer> dq = new ArrayDeque<>(bridge_length);
        int totalWeight = 0;
        int idx = 0;
        for (int i=0; i<bridge_length; i++) dq.add(0);
        
        while (!dq.isEmpty()) {
            answer++;
            totalWeight -= dq.pollFirst();
            
            if (idx < truck_weights.length && truck_weights[idx] + totalWeight <= weight) {
                totalWeight += truck_weights[idx];
                dq.addLast(truck_weights[idx++]);
            } else if (idx < truck_weights.length) dq.addLast(0);
        }
        
        return answer;
    }
}