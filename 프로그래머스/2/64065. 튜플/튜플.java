import java.util.*;

class Solution {
    public int[] solution(String s) {
        String[] arr = s.substring(1, s.length() - 1).split("\\},\\{");
        arr[0] = arr[0].substring(1);
        arr[arr.length - 1] = arr[arr.length - 1].substring(0, arr[arr.length - 1].length() - 1);
        
        Arrays.sort(arr, (o1, o2) -> {
            return o1.length() - o2.length();
        });
        
        Set<Integer> set = new HashSet<>();
        List<Integer> answer = new ArrayList<>();
        
        for (String numbers : arr) {
            String[] number = numbers.split(",");
            for (String num : number) {
                int n = Integer.parseInt(num);
                if (set.add(n)) answer.add(n);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}