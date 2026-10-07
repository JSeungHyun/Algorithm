class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(0, 0, target, numbers);
    }
    
    private int dfs(int depth, int sum, int target, int[] numbers) {
        if (depth == numbers.length) {
            return sum == target ? 1 : 0;
        }
        
        return dfs(depth + 1, sum + numbers[depth], target, numbers)
             + dfs(depth + 1, sum - numbers[depth], target, numbers);
    }
}