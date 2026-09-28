import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        
        int[] a = new int[]{1, 2, 3, 4, 5};
        int[] b = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int countA = 0;
        int countB = 0;
        int countC = 0;
        
        for (int i=0; i<answers.length; i++) {
            if (a[i % a.length] == answers[i]) countA++;
            if (b[i % b.length] == answers[i]) countB++;
            if (c[i % c.length] == answers[i]) countC++;
        }
        
        int count = Math.max(Math.max(countA, countB), countC);
        
        if (count == countA) answer.add(1);
        if (count == countB) answer.add(2);
        if (count == countC) answer.add(3);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}