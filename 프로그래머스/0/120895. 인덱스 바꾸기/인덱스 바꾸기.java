class Solution {
    public String solution(String my_string, int num1, int num2) {
        String[] s = my_string.split("");
        String tmp = "";
        String answer =  "";
        
        tmp = s[num1];
        s[num1] = s[num2];
        s[num2] = tmp;
        
        answer = String.join("", s);
        
        return answer;
    }
}