import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] arr = new String[numbers.length];
        for (int i=0; i<numbers.length; i++) {
            arr[i] = Integer.toString(numbers[i]);
        }
        Arrays.sort(arr, (o1, o2) -> {
            return (o2 + o1).compareTo(o1 + o2);
        });
        
        StringBuilder sb = new StringBuilder();
        for (String s : arr) sb.append(s);
        
        String answer = sb.toString();
        
        return answer.startsWith("0") ? "0" : answer;
    }
}