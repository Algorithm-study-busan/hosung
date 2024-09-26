class Solution {
    public long calTime(int[] diffs, int[] times, int level) {
        long ret = 0;
        ret += Math.max(1, diffs[0] - level) * times[0];
        
        for (int i=1;i<times.length;i++) {
            ret += Math.max(0, diffs[i] - level) * (times[i-1] + times[i]) + times[i];
        }
        
        return ret;
    }
    
    public int solution(int[] diffs, int[] times, long limit) {
        int lo = 1;
        int hi = 100000;
        
        while (lo <= hi) {
            int mid = (lo + hi)/2;
            
            long time = calTime(diffs, times, mid);
            if (time > limit) lo = mid+1;
            else hi = mid-1;
        }
        return lo;
    }
}