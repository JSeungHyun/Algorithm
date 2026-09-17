import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        
        for (int i : d) {
            if (i <= budget) {
                answer++;
                budget -= i;
            } else break;
        }
        
        return answer;
    }
}