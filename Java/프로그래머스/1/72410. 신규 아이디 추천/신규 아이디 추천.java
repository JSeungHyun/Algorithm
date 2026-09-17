class Solution {
    public String solution(String new_id) {
        // 1단계 소문자 치환
        new_id = new_id.toLowerCase();
        
        // 2단계
        new_id = new_id.replaceAll("[^a-z0-9-_.]", "");
        
        // 3단계
        new_id = new_id.replaceAll("\\.{2,}", ".");
        
        // 4단계
        new_id = new_id.replaceAll("^\\.|\\.$", "");
        
        // 5단계
        if (new_id.isEmpty()) {
            new_id = "a";
        }
        
        // 6단계
        if (new_id.length() >= 16) {
            new_id = new_id.substring(0, 15).replaceAll("[.]$", "");
        }
        
        // 7단계
        StringBuilder sb = new StringBuilder(new_id);
        while (sb.length() <= 2) sb.append(sb.charAt(sb.length() - 1));
        
        return sb.toString();
    }
}