import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] citations) {
        // int[]를 Integer[]로 변환하여 내림차순 정렬
        Integer[] citationsArr = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(citationsArr, Collections.reverseOrder());

        int answer = 0;
        for (int i = 0; i < citationsArr.length; i++) {
            if (citationsArr[i] >= i + 1) {
                answer = i + 1;
            } else {
                break; // 더 이상 조건을 만족하지 않으면 반복 종료
            }
        }

        return answer;
    }
}
