import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> set = new HashSet<>(
            Arrays.stream(nums).boxed().collect(Collectors.toSet())
        );
        int answer = set.size();
        if (answer > nums.length/2){
            answer = nums.length/2;
        }
        return answer;
    }
}
