import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        Deque<Integer> dq = new ArrayDeque<>();
        
        for (int move : moves) {
            int col = move - 1;
            for (int row = 0; row < n; row++) {
                if (board[row][col] != 0) {
                    int doll = board[row][col];
                    board[row][col] = 0;
                    
                    if (!dq.isEmpty() && dq.peekLast() == doll) {
                        dq.pollLast();
                        answer += 2;
                    } else {
                        dq.addLast(doll);
                    }
                    break;
                }
            }
        }
        
        return answer;
    }
}