import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Deque<Integer> dq = new ArrayDeque<>();
        int n = prices.length;
        
        for (int i=n-1; i>=0; i--) {
            int p = prices[i];
            
            while (!dq.isEmpty() && p <= prices[dq.peekFirst()]) {
                dq.pollFirst();
            }
            
            if (dq.isEmpty()) {
                answer[i] = (n - 1) - i;
            } else {
                answer[i] = dq.peekFirst() - i;
            }
            
            dq.addFirst(i);
        }
        
        return answer;
    }
}