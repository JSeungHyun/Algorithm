import java.util.*;

class Solution {
    public String solution(String number, int k) {
        int targetSize = number.length() - k;
        StringBuilder sb = new StringBuilder();
        
        for (char c : number.toCharArray()) {
            while (sb.length() > 0 && k > 0 && sb.charAt(sb.length() - 1) < c) {
                sb.setLength(sb.length() - 1);
                k--;
            }
            sb.append(c);
        }
        
        return sb.toString().substring(0, targetSize);
    }
}