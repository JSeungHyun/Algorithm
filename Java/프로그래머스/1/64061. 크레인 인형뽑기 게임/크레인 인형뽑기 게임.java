import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        int k;
        boolean flag;
        Deque<Integer> dq = new ArrayDeque<>();
        
        for (int move : moves) {
            int idx = 0;
            while (idx < n) {
                if (board[idx][move - 1] != 0) { // 인형 있으면 진입
                    flag = true;
                    k = board[idx][move - 1];
                    if (!dq.isEmpty()) {
                        if (dq.peekLast() == k) { // 같은 인형일경우
                            dq.pollLast();
                            answer += 2;
                            flag = false;
                        }
                    }
                    board[idx][move - 1] = 0;
                    if (flag) dq.addLast(k); 
                    break; // 인형있으면 다음 MOVE
                }
                idx++; // 인형없으면 탐색
            }
        }
        
        return answer;
    }
}