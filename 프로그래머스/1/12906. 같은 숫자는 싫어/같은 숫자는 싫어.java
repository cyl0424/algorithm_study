import java.util.*;

import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answerList = new ArrayList<Integer>();
        
        answerList.add(arr[0]);
        
        for (int i = 1; i < arr.length; i++){
            if(arr[i-1] != arr[i]){
                answerList.add(arr[i]);
            }
        }

        return answerList.stream().mapToInt(i -> i).toArray();
    }
}