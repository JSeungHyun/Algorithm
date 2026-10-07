class Solution {
    public int[] solution(int brown, int yellow) {
        for (int h = 1; h * h <= yellow; h++) {
            if (yellow % h == 0) {
                int w = yellow / h;
                
                if ((w + h) * 2 + 4 == brown) {
                    return new int[]{w + 2, h + 2};
                }
            }
        }
        
        return new int[0];
    }
}