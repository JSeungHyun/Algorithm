import java.util.*;

class Solution {
    public int solution(String s) {
        Deque<Character> dq = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if (dq.isEmpty()) dq.addLast(c);
            else {
                if (c == dq.peekLast()) dq.pollLast();
                else dq.addLast(c);
            }
        }
        
        return dq.isEmpty() ? 1 : 0;
    }
}