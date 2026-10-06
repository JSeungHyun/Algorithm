import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        
        for (int i=0; i<phone_book.length - 1; i++) {
            String phone = phone_book[i];
            String target = phone_book[i + 1];
            
            if (target.startsWith(phone)) return false;
        }
        return true;
    }
}