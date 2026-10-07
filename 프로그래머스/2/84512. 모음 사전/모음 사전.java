class Solution {
    static Character[] words = new Character[]{'A', 'E', 'I', 'O', 'U'};
    static int answer;
    static int depth;
    
    public int solution(String word) {
        answer = 0;
        depth = 0;
        search(new StringBuilder(), word);
        return answer;
    }
    
    public boolean search(StringBuilder sb, String target) {
        if (sb.toString().equals(target)) {
            answer = depth;
            return true;
        }
        if (sb.length() == 5) return false;
        
        for (int i=0; i<5; i++) {
            depth++;
            sb.append(words[i]);
            if (search(sb, target)) return true;
            sb.deleteCharAt(sb.length() - 1);
        }
        
        return false;
    }
}