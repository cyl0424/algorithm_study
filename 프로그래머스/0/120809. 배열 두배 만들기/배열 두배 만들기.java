class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        int cnt = 0;
        
        for (int num: numbers){
            answer[cnt] = num * 2;
            cnt ++;
        }
        return answer;
    }
}