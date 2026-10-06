import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        StringBuilder sb = new StringBuilder(s);
        
        for (int i=0; i<s.length(); i++) {
            Deque<Character> dq = new ArrayDeque<>();
            boolean flag = true;
            
            for (char c : sb.toString().toCharArray()) {
                if (dq.isEmpty() && (c == ')' || c == ']' || c == '}')) {
                    flag = false;
                } else if (c == '(' || c == '[' || c == '{') {
                    dq.addLast(c);
                } else if (c == ')') {
                    char temp = dq.pollLast();
                    if (temp != '(') flag = false;
                } else if (c == ']') {
                    char temp = dq.pollLast();
                    if (temp != '[') flag = false;
                } else if (c == '}') {
                    char temp = dq.pollLast();
                    if (temp != '{') flag = false;
                }
                
                if (!flag) break;
            }
            
            if (dq.isEmpty() && flag) answer++;
            sb.append(sb.toString().charAt(0));
            sb.deleteCharAt(0);
        }
        
        return answer;
    }
}