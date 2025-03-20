import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] numbersString = new String[numbers.length];
        
        for (int i = 0; i < numbers.length; i++){
            numbersString[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(numbersString, (a, b) -> (b+a).compareTo(a+b));
        
        answer = String.join("", numbersString);
        
        if (answer.startsWith("0")){
            answer = "0";
        }
        
        return answer;
    }
}