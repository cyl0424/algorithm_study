class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] char_list = my_string.toCharArray();
        
        char[] reverse = new char[char_list.length];
        
        for (int i = char_list.length; i > 0; i--){
            reverse[i-1] = char_list[char_list.length - i];
        }
        
        answer = new String(reverse);
        return answer;
    }
}