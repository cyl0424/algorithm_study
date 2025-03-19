import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int midIdx = array.length / 2;
        int answer = array[midIdx];
        return answer;
    }
}