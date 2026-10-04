class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder(numbers.length);
        boolean isRightHanded = "right".equals(hand);
        
        int left = 9;   // '*' 위치 (인덱스 9)
        int right = 11; // '#' 위치 (인덱스 11)
        
        for (int num : numbers) {
            int target = (num == 0) ? 10 : num - 1;
            boolean moveRight;
            
            if (target % 3 == 0) {         // 1, 4, 7 -> 왼손
                moveRight = false;
            } else if (target % 3 == 2) {  // 3, 6, 9 -> 오른손
                moveRight = true;
            } else {                       // 2, 5, 8, 0 -> 거리 비교
                int leftDist = getDistance(left, target);
                int rightDist = getDistance(right, target);
                
                if (leftDist != rightDist) {
                    moveRight = leftDist > rightDist;
                } else {
                    moveRight = isRightHanded;
                }
            }
            
            if (moveRight) {
                answer.append('R');
                right = target;
            } else {
                answer.append('L');
                left = target;
            }
        }
        
        return answer.toString();
    }
    
    private int getDistance(int cur, int target) {
        return Math.abs((cur / 3) - (target / 3)) + Math.abs((cur % 3) - (target % 3));
    }
}