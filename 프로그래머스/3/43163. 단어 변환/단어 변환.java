import java.util.*;

class Solution {
    static int answer;
    static Map<String, List<String>> map;
    static Map<String, Boolean> visited;
    
    public int solution(String begin, String target, String[] words) {
        answer = Integer.MAX_VALUE;
        map = new HashMap<>();
        visited = new HashMap<>();
        String[] wordArr = Arrays.copyOf(words, words.length + 1);
        wordArr[wordArr.length - 1] = begin;
        int wl = words[0].length();
        
        for (int i=0; i<wordArr.length; i++) {
            String s = wordArr[i];
            visited.put(s, false);
            
            for (int j=i+1; j<wordArr.length; j++) {
                String e = wordArr[j];
                int diff = 0;
                
                for (int k=0; k<wl; k++) {
                    if (s.charAt(k) != e.charAt(k)) diff++;
                    if (diff > 1) break;
                }
                
                if (diff == 1) {
                    List<String> sList = map.getOrDefault(s, new ArrayList<>());
                    sList.add(e);
                    map.put(s, sList);
                    
                    List<String> eList = map.getOrDefault(e, new ArrayList<>());
                    eList.add(s);
                    map.put(e, eList);
                }
            }
        }
        
        visited.put(begin, true);
        dfs(begin, target, 0);
        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
    
    static void dfs(String cur, String target, int v) {
        List<String> arr = map.getOrDefault(cur, new ArrayList<>());
        
        for (String s : arr) {
            System.out.println(s);
            if (s.equals(target)) {
                answer = Math.min(answer, v + 1);
                return;
            }
            if (visited.get(s)) continue;
            visited.put(s, true);
            dfs(s, target, v+1);
            visited.put(s, false);
        }
    }
}