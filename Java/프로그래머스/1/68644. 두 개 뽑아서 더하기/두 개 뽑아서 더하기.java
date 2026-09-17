import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> arr = new ArrayList<>();
        
        for (int i=0; i<numbers.length; i++) {
            for (int j=i+1; j<numbers.length; j++) {
                arr.add(numbers[i] + numbers[j]);
            }
        }
        
        return arr.stream().distinct().sorted().mapToInt(i -> i).toArray();
    }
}