import java.util.*;

class Solution {
    public int[] solution(int[][] dice) {
        int N = dice.length;
        
        Map<List<Integer>, List<Integer>> results = new HashMap<>();
        
        int[] idxes = new int[N];
        
        for (int i=0;i<N;i++) idxes[i] = i;
        
        List<List<Integer>> combinations = new ArrayList<>();
        combine(idxes, N/2, 0, new ArrayList<>(), combinations);
        
        for (List<Integer> combination : combinations) {
            List<Integer> result = new ArrayList<>();
            getResult(combination, result, 0, 0, dice);
            Collections.sort(result);
            results.put(combination, result);
        }
        
        
        int ans[] = new int[N/2];
        
        int maxCount = 0;
        
        for (List<Integer> combination : combinations) {
            List<Integer> another = getAnother(combination, N);
            
            List<Integer> result_cur = results.get(combination);
            List<Integer> result_another = results.get(another);
            
            int tmp = 0;
            for (int x : result_cur) {
                tmp += lowerBound(result_another, x);
            }
            
            if (maxCount < tmp) {
                for (int i=0;i<N/2;i++) {
                    ans[i] = combination.get(i)+1;
                }
                maxCount = tmp;
            }
        }
        
        return ans;
    }
    
    public int lowerBound(List<Integer> result, int x) {
        int lo = 0;
        int hi = result.size()-1;
        
        while (lo <= hi) {
            int mid = (lo+hi)/2;
            
            if (result.get(mid) < x) lo = mid+1;
            else hi = mid-1;
        }
        
        return lo;
    }
    
    public List<Integer> getAnother(List<Integer> combination, int N) {
        boolean[] selected = new boolean[N];
        for (int n : combination) {
            selected[n] = true;
        }
        
        List<Integer> ret = new ArrayList<>();
        
        for (int i=0;i<N;i++) {
            if (!selected[i]) ret.add(i);
        }
        return ret;
    }
    
    public void getResult(List<Integer> combination, List<Integer> result, int idx, int sum, int[][] dice) {
        if (idx == combination.size()) {
            result.add(sum);
            return;
        }
        
        for (int i=0;i<6;i++) {
            getResult(combination, result, idx+1, sum + dice[combination.get(idx)][i], dice);
        }
    }
    
    public void combine(int[] idxes, int r, int start, List<Integer> current, List<List<Integer>> combinations) {
        if (current.size() == r) {
            combinations.add(new ArrayList<>(current));
            return;
        }
        
        for (int i=start;i<idxes.length;i++) {
            current.add(idxes[i]);
            combine(idxes, r, i+1, current, combinations);
            current.remove(current.size()-1);
        }
    }
}