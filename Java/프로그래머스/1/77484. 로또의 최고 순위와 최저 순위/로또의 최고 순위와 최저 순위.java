import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int zeroCount = 0;
        int match = 0;
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : win_nums) map.put(num, 1);
        
        for (int i : lottos) {
            if (i == 0) zeroCount++;
            if (map.getOrDefault(i, 0) == 1) match++;
        }
        
        int[] answer = new int[2];
        answer[0] = 7 - match - zeroCount == 7 ? 6 : 7 - match - zeroCount;
        answer[1] = match == 0 ? 6 : 7 - match;
        
        return answer;
    }
}