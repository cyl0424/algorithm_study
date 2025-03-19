class Solution {
    public int solution(int n, int k) {
        int answer = 12000 * n + 2000 * k;
        int freeDrink = n / 10;
        
        answer -= freeDrink * 2000;
        
        return answer;
    }
}