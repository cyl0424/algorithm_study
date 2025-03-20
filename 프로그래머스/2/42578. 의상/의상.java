import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothesMap = new HashMap<>();
        int answer = 1;
        
        for (String[] cloth: clothes){
            clothesMap.put(cloth[1], clothesMap.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (Integer value: clothesMap.values()){
            answer *= value + 1;
        }
        
        return answer -1;
    }
}