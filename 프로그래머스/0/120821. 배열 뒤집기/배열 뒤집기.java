import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        
        for (int i = answer.length; i > 0; i--){
            answer [i-1] = num_list[answer.length-i];
        }
        return answer;
    }
}