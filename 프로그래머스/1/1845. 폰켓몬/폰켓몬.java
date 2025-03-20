import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> set = new HashSet<>(
            Arrays.stream(nums).boxed().collect(Collectors.toSet())
        );
        int answer = set.size();
        if (answer > nums.length/2){
            answer = nums.length/2;
        }
        return answer;
    }
}
