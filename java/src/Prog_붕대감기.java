class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int cur_attack_idx = 0;
        int max_health = health;
        
        int tmp = 0;
        for (int time=0;time<=attacks[attacks.length-1][0];time++) {
            if (time == attacks[cur_attack_idx][0]) {
                health -= attacks[cur_attack_idx][1];
                if (health <= 0) return -1;
                cur_attack_idx++;
                tmp = 0;
            } else {
                health = Math.min(max_health, bandage[1] + health);
                tmp ++;
                
                if (tmp == bandage[0]) {
                    health = Math.min(max_health, bandage[2] + health);
                    tmp = 0;
                }
            }
        }
        
        return health;
    }
}