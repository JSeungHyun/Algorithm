import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque dq = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(') dq.addLast('(');
            else {
                if (dq.isEmpty()) return false;
                dq.pollLast();
            }
        }
        
        return dq.isEmpty() ? true : false;
    }
}