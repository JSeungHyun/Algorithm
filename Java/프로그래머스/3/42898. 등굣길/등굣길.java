class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];
        
        for (int[] puddle : puddles) dp[puddle[1]-1][puddle[0]-1] = -1;
        
        for (int i=0; i<n; i++) {
            if (dp[i][0] == -1) break; 
            dp[i][0] = 1;
        }
        
        for (int i=0; i<m; i++) {
            if (dp[0][i] == -1) break; 
            dp[0][i] = 1;
        }
        
        for (int y=1; y<n; y++) {
            for (int x=1; x<m; x++) {
                if (dp[y][x] == -1) continue;
                
                int left = dp[y][x-1] == -1 ? 0 : dp[y][x-1];
                int up = dp[y-1][x] == -1 ? 0 : dp[y-1][x];
                dp[y][x] = (left + up) % 1000000007;
            }
        }
        
        return dp[n-1][m-1];
    }
}