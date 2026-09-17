class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            int i = (int) c + n;
            if (Character.isLowerCase(c)) {
                if (i > (int) 'z') {
                    int t = i - (int) 'z' + (int) 'a' - 1;
                    sb.append((char) t);
                } else sb.append((char) i);
            } else if (Character.isUpperCase(c)) {
                if (i > (int) 'Z') {
                    int t = i - (int) 'Z' + (int) 'A' - 1;
                    sb.append((char) t);
                } else sb.append((char) i);
            } else {
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}