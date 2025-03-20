import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answerList = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++){
            queue.offer((int)Math.ceil((100.0 - progresses[i])/speeds[i]));
        }
        
        while(!queue.isEmpty()){
            int passedDays = queue.poll();
            int cnt = 1;
            
            while(!queue.isEmpty() && queue.peek() <= passedDays){
                queue.poll();
                cnt++;
            }
            
            answerList.add(cnt);
        }
        
        int[] answer = answerList.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}