class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int depth = triangle.length - 1;
        
        while(depth > 0){
            for (int i = 0; i < depth; i++){
                triangle[depth-1][i] += (int) Math.max(triangle[depth][i], triangle[depth][i+1]);
            }
            
            depth -= 1;
        }
        
        answer = triangle[0][0];
        return answer;
    }
}