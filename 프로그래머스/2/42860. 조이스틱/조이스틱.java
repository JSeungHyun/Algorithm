class Solution {
    public int solution(String name) {
        int len = name.length();
        int moveCount = len - 1;
        int changeCount = 0;
        
        for (int i=0; i<len; i++) {
            changeCount += getChangeCount(name.charAt(i));
            int next = i + 1;
            while (next < len && name.charAt(next) == 'A') next++;
            
            int turnBack = (i * 2) + (len - next);
            int turnFront = ((len - next) * 2) + i;

            moveCount = Math.min(moveCount, Math.min(turnBack, turnFront));
        }
        
        return moveCount + changeCount;
    }
    
    static int getChangeCount(char c) {
        return Math.min(c - 'A', 'Z' - c + 1);
    }
}