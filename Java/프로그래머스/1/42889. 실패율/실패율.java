import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        double[][] failRate = new double[N][2];
        int[] failCount = new int[N + 2];
        int total = stages.length;
        
        for (int stage : stages) failCount[stage]++;
        
        for (int i=1; i<=N; i++) {
            failRate[i - 1][0] = i;
            failRate[i - 1][1] = total != 0 ? (double) failCount[i] / total : 0;
            total -= failCount[i];
        }
        
        Arrays.sort(failRate, (o1, o2) -> {
            if (o1[1] == o2[1]) return Double.compare(o1[0], o2[0]);
            return Double.compare(o2[1], o1[1]);
        });
        
        for (int i=0; i<N; i++) {
            answer[i] = (int) failRate[i][0];
        }
        
        return answer;
    }
}