import java.util.*;

class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        String[] my_strings = my_string.split("");
        for (int indice : indices) {
            my_strings[indice] = "";
        }
        for (String s : my_strings) {
            answer += s;
        }
        return answer;
    }
}