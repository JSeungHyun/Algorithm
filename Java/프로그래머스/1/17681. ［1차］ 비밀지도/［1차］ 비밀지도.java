import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int y=0; y<n; y++) {
            int combined = arr1[y] | arr2[y];
            String num = String.format("%" + n + "s", Integer.toString(combined, 2));
            answer[y] = num.replace('0', ' ').replace('1', '#');
        }
        
        return answer;
    }
}