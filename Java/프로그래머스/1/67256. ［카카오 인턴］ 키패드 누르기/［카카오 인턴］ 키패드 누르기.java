import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        int[] position = new int[10];
        position[0] = 10;
        for (int i=1; i<=9; i++) position[i] = i - 1;
        
        int left = 9;
        int right = 11;
        
        for (int n : numbers) {
            n = position[n];
            if (n % 3 == 0) { // 왼손 이동
                answer.append("L");
                left = n;
            } else if (n % 3 == 2) { // 오른손 이동
                answer.append("R");
                right = n;
            } else {
                int leftDistance = getDistance(left, n);
                int rightDistance = getDistance(right, n);
                
                if (leftDistance < rightDistance) {
                    answer.append("L");
                    left = n;
                } else if (leftDistance > rightDistance) {
                    answer.append("R");
                    right = n;
                } else {
                    if (hand.equals("right")) {
                        answer.append("R");
                        right = n;
                    } else {
                        answer.append("L");
                        left = n;
                    }
                }
            }
        }
        
        return answer.toString();
    }
    
    private int getDistance(int cur, int target) {
        return Math.abs((cur % 3) - (target % 3)) + Math.abs((cur / 3) - (target / 3));
    }
}