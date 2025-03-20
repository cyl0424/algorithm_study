import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        Queue<Integer> pq = new PriorityQueue<>();
        int currentScoville = 0;
        int answer = 0;
        
        for (int i = 0; i < scoville.length; i++){
            pq.offer(scoville[i]);
        }
        
        while (pq.peek() < K && pq.size() > 1){
            int leastSpicy = pq.poll();
            int leastSpicy2 = pq.poll();
            
            currentScoville = leastSpicy + leastSpicy2*2;
            pq.offer(currentScoville);
            
            answer++;
        }
        
        if (pq.peek() < K){
            answer = -1;
        }
        
        return answer;
    }
}