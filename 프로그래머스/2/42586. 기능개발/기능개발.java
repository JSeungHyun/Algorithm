import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Deque<Integer> pgr_dq = new ArrayDeque<>();
        Deque<Integer> speed_dq = new ArrayDeque<>();
        
        for (int i=0; i<progresses.length; i++) {
            pgr_dq.addLast(progresses[i]);
            speed_dq.addLast(speeds[i]);
        }
        
        while (!pgr_dq.isEmpty()) {
            int progress = pgr_dq.pollFirst();
            int speed = speed_dq.pollFirst();
            int day = (int) Math.ceil((100.0 - progress) / speed);
            int cnt = 1;
            
            while (!pgr_dq.isEmpty() &&
                   (int) Math.ceil((100.0 - pgr_dq.peekFirst()) / speed_dq.peekFirst()) <= day) {
                pgr_dq.pollFirst();
                speed_dq.pollFirst();
                cnt++;
            }
            
            answer.add(cnt);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}