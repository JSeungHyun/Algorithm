import java.util.*;

class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(0, 0, target, numbers);
        return answer;
    }
    
    public int dfs(int depth, int v, int target, int[] numbers) {
        if (depth == numbers.length) {
            if (v == target) answer++;
            return 0;
        }
        dfs(depth + 1, v + numbers[depth], target, numbers);
        dfs(depth + 1, v - numbers[depth], target, numbers);
        return 0;
    }
}