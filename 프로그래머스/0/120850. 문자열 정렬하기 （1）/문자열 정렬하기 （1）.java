import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        String[] new_string = my_string.replaceAll("[^0-9]", "").split("");
        int[] answer = new int[new_string.length];
        
        for (int i = 0; i < new_string.length; i++){
            answer[i] = Integer.parseInt(new_string[i]);
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}