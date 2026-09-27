import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int[] command;
        int[] temp;
        
        for (int i=0; i<commands.length; i++) {
            command = commands[i];
            temp = Arrays.copyOfRange(array, command[0] - 1, command[1]);
            Arrays.sort(temp);
            answer[i] = temp[command[2] - 1];
            
        }
        
        return answer;
    }
}