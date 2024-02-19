import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        ArrayList<Integer> stack = new ArrayList<>();
        for (int num : arr) {
            if (stack.size() == 0) {
                stack.add(num);
            }
            else {
                if (stack.get(stack.size()-1).intValue() != num) {
                    stack.add(num);
                }
            }
        }
        
        answer = new int[stack.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = stack.get(i).intValue();
        }

        return answer;
    }
}