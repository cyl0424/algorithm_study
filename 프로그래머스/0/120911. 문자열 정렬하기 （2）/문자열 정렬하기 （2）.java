import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = my_string.toLowerCase();
        char[] answerArray = answer.toCharArray();
        
        Arrays.sort(answerArray);
        
        answer = new String(answerArray);
        
        return answer;
    }
}