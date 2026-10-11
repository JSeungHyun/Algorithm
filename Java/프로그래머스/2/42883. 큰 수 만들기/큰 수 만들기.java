import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        int targetNumber = number.length() - k;
        
        for (int i=0; i<number.length(); i++) {
            while (!sb.isEmpty() && k > 0 && sb.charAt(sb.length() - 1) < number.charAt(i)) {
                k--;
                sb.deleteCharAt(sb.length() - 1);
            }
            sb.append(number.charAt(i));
        }
        
        return sb.toString().substring(0, targetNumber);
    }
}