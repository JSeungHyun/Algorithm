class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;
        int[][] dp = new int[n][];

        for (int i = 0; i < n; i++) {
            dp[i] = new int[i + 1];
        }
        
        dp[0][0] = triangle[0][0];
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                if (j != 0)
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + triangle[i][j]);    
                if (j != i)
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j] + triangle[i][j]);
            }
        }
        
        int answer = 0;
        for (int v : dp[n - 1]) answer = Math.max(answer, v);
        return answer;
    }
}