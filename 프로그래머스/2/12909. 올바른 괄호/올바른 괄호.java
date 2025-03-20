import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> check = new Stack<>();
        
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
            if (c == '('){
                check.push(c);
            } else {
                if (check.isEmpty()){
                    return false;
                } else{
                    check.pop();
                }
            }
        }

        return check.isEmpty();
    }
}