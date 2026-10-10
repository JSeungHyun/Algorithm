import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int left = 0;
        int right = people.length - 1;
        Arrays.sort(people);
        
        // right 를 감소시키면서 태우기
        while (left <= right) {
            // left를 함께 태울 수 있을 때에만 left++
            if (people[right--] + people[left] <= limit) left++;
            answer++;
        }
        
        return answer;
    }
}