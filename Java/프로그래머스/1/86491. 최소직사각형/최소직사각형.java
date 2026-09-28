import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxWidth = 0;
        int maxHeight = 0;
        int temp;
        
        for (int[] size : sizes) {
            if (size[1] > size[0]) {
                temp = size[1];
                size[1] = size[0];
                size[0] = temp;
            }
            
            maxWidth = Math.max(maxWidth, size[0]);
            maxHeight = Math.max(maxHeight, size[1]);
        }
        
        return maxWidth * maxHeight;
    }
}