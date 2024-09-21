import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        Map<String, Integer> toIdx = new HashMap<>();
        
        for (int i=0;i<friends.length;i++) {
            toIdx.put(friends[i], i);
        }
        
        int[] giftScore = new int[friends.length];
        int[][] giftBoard = new int[friends.length][friends.length];
        
        for (String gift : gifts) {
            String[] giftSplited = gift.split(" ");
            int a = toIdx.get(giftSplited[0]);
            int b = toIdx.get(giftSplited[1]);
            
            giftScore[a]++;
            giftScore[b]--;
            
            giftBoard[a][b]++; 
        }
        
        int[] giftNum = new int[friends.length];
        
        for (int a = 0; a < friends.length; a++) {
            for (int b = a+1; b < friends.length; b++) {
                if (giftBoard[a][b] > giftBoard[b][a]) giftNum[a]++;
                else if (giftBoard[a][b] < giftBoard[b][a]) giftNum[b]++;
                else {
                    if (giftScore[a] > giftScore[b]) giftNum[a]++;
                    else if (giftScore[a] < giftScore[b]) giftNum[b]++;
                }
            }
        }
        
        int ans = 0;
        
        for (int i=0;i<friends.length;i++) {
            ans = Math.max(ans, giftNum[i]);
        }
        
        return ans;
    }
}