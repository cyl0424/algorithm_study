class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        char[] charList = my_string.toCharArray();
        char[] answerList = new char[charList.length * n];
        
        for (int i = 0; i < charList.length; i++){
            for (int j = 0; j < n; j++){
                answerList[n*i + j] = charList[i];
            }
        }
        answer = new String(answerList);
        return answer;
    }
}