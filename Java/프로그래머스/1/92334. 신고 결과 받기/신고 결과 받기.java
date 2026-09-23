import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, Set<String>> map = new HashMap<>();
        Map<String, Integer> position = new HashMap<>();
        
        for (int i=0; i<id_list.length; i++) position.put(id_list[i], i);
        
        for (String r : report) {
            String[] spl = r.split(" ");
            String reporter = spl[0];
            String target = spl[1];
            
            Set<String> set = map.getOrDefault(target, new HashSet<>());
            set.add(reporter);
            map.put(target, set);
        }
        
        for (Map.Entry<String, Set<String>> entry : map.entrySet()) {
            if (entry.getValue().size() < k) continue;
            for (String s : entry.getValue()) {
                answer[position.get(s)]++;
            }
        }
        
        return answer;
    }
}