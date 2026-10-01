import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] stageCount = new int[N+2];
        int total = stages.length;
        
        for (int stage : stages) {
            stageCount[stage]++;
        }
        
        List<Stage> stageList = new ArrayList<>();
        for (int i=1; i<=N; i++) {
            double rate = total == 0 ? 0 : (double) stageCount[i] / total;
            Stage stage = new Stage(i, rate);
            stageList.add(stage);
            total -= stageCount[i];
        }
        
        Collections.sort(stageList);
        
        int[] answer = new int[N];
        int idx=0;
        
        for (Stage s : stageList) {
            answer[idx++] = s.n;
        }
        
        return answer;
    }
    
    static class Stage implements Comparable<Stage> {
        int n;
        double rate;
        
        Stage(int n, double rate) {
            this.n = n;
            this.rate = rate;
        }
        
        @Override
        public int compareTo(Stage o) {
            if (Double.compare(o.rate, this.rate) == 0) return Integer.compare(this.n, o.n);
            return Double.compare(o.rate, this.rate);
        }
    }
}