import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long answer = (long) n * times[times.length - 1];
        long left = 1;
        long right = answer;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            long target = 0;
            
            for (int time : times) {
                target += mid / time;
            }
            
            if (target >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        
        return answer;
    }
}