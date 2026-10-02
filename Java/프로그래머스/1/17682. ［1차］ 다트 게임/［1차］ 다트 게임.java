import java.util.*;

class Solution {
    public int solution(String dartResult) {
        int[] score = new int[3];
        int idx = -1;
        int len = dartResult.length();
        char c;
        
        for (int i = 0; i < len; i++) {
            c = dartResult.charAt(i);
            if (Character.isDigit(c)) {
                idx++;
                if (c == '1' && Character.isDigit(dartResult.charAt(i + 1))) {
                    score[idx] = 10;
                    i++;
                } else score[idx] = c - '0';
            } else if (c == 'S') {
                // 스킵
            } else if (c == 'D') {
                score[idx] *= score[idx];
            } else if (c == 'T') {
                score[idx] *= score[idx] * score[idx];
            } else if (c == '#') {
                score[idx] *= -1;
            } else { // c == '*'
                score[idx] *= 2;
                if (idx > 0) score[idx - 1] *= 2;
            }
        }
        
        return score[0] + score[1] + score[2];
    }
}