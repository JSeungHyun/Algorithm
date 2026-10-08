import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        boolean[] visited = new boolean[words.length];
        Deque<Node> dq = new ArrayDeque<>();
        dq.addLast(new Node(begin, 0));

        while (!dq.isEmpty()) {
            Node cur = dq.pollFirst();

            if (cur.word.equals(target)) {
                return cur.step;
            }

            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && canConvert(cur.word, words[i])) {
                    visited[i] = true;
                    dq.addLast(new Node(words[i], cur.step + 1));
                }
            }
        }

        return 0;
    }

    private boolean canConvert(String s1, String s2) {
        int diff = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) diff++;
            if (diff > 1) return false;
        }
        return diff == 1;
    }

    static class Node {
        String word;
        int step;

        Node(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }
}