import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int cnt = 0;
        
        for (int[] command: commands){
            int[] subArray = Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(subArray);
            int result = subArray[command[2]-1];
            answer[cnt] = result;
            
            cnt++;
        }
        
        return answer;
    }
}