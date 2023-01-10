import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for (int work : works) {
            queue.add(work);
        }
        while(n>0){
            n--;
            queue.add(queue.poll() - 1);
        }
        for (Integer i : queue) {
            if(i>0) answer += Math.pow(i,2);
        }
        return answer;
    }
}