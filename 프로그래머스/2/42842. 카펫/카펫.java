import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int w = yellow;
        int h = 1;
        
        while (w >= h) {
            if (getBrown(w, h) == brown) {
                answer[0] = w + 2;
                answer[1] = h + 2;
                break;
            }
            while (true) {
                h++;
                if (yellow % h == 0) {
                    w = yellow / h;
                    break;
                }
            }
        }
        
        return answer;
    }
    
    static int getBrown(int h, int w) {
        return (h * 2) + ((w + 2) * 2);
    }
}