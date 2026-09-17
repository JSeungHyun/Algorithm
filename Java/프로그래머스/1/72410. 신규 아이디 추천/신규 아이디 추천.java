class Solution {
    public String solution(String new_id) {
        // 1단계 소문자 치환
        new_id = new_id.toLowerCase();
        
        // 2단계
        StringBuilder sb = new StringBuilder();
        for (char c : new_id.toCharArray()) {
            if (Character.isDigit(c) || Character.isAlphabetic(c) || 
                c == '-' || c == '_' || c == '.') {
                sb.append(c);
            }
        }
        new_id = sb.toString();
        
        // 3단계
        while (new_id.contains("..")) {
            new_id = new_id.replace("..", ".");
        }
        
        // 4단계
        sb = new StringBuilder(new_id);
        if (sb.length() > 0 && sb.charAt(0) == '.') 
            sb.deleteCharAt(0);
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '.') 
            sb.deleteCharAt(sb.length() - 1);
        
        // 5단계
        if (sb.length() == 0) sb.append("a");
        
        // 6단계
        if (sb.length() > 15) sb.setLength(15);
        if (sb.charAt(sb.length() - 1) == '.') sb.deleteCharAt(sb.length() - 1);
        
        // 7단계
        while (sb.length() <= 2) sb.append(sb.charAt(sb.length() - 1));
        
        return sb.toString();
    }
}