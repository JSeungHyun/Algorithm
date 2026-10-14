import java.util.*;

class Solution {
    int solution(int[][] land) {
        int n = land.length;
        int[][] dp = new int[n][4];
        
        for (int i=0; i<4; i++) dp[0][i] = land[0][i];
        
        for (int i=1; i<n; i++) {
            dp[i][0] = Math.max(dp[i][0], Math.max(Math.max(dp[i - 1][1], dp[i - 1][2]), dp[i-1][3]) + land[i][0]);
            dp[i][1] = Math.max(dp[i][1], Math.max(Math.max(dp[i - 1][0], dp[i - 1][2]), dp[i-1][3]) + land[i][1]);
            dp[i][2] = Math.max(dp[i][2], Math.max(Math.max(dp[i - 1][0], dp[i - 1][1]), dp[i-1][3]) + land[i][2]);
            dp[i][3] = Math.max(dp[i][3], Math.max(Math.max(dp[i - 1][0], dp[i - 1][1]), dp[i-1][2]) + land[i][3]);
        }
        
        int answer = 0;
        for (int i=0; i<4; i++) answer = Math.max(answer, dp[n - 1][i]);
        return answer;
    }
}