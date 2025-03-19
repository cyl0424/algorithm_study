import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int answer = numbers[0] * numbers[1];
        int answer2 = numbers[numbers.length-1] * numbers[numbers.length-2];
        
        if (answer < answer2){
            answer = answer2;
        }
        return answer;
    }
}