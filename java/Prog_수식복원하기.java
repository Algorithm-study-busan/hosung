import java.util.*;

class Solution {
    public int getMaxDegit(String expression) {
        String[] ops = expression.split(" ");
        
        
        List<String> arr = new ArrayList<>();
        arr.add(ops[0]);
        arr.add(ops[2]);
        if (!ops[4].equals("X")) arr.add(ops[4]); 
        
        int ret = 0;
        for (String op : arr) {
            for (char c : op.toCharArray()) {
                ret = Math.max(ret, c-'0');
            }
        }
        
        return ret;
    }
    
    public int toNum(String n, int k) {
        int ret = 0;
        int e=1;
        for (int i=n.length()-1;i>=0;i--) {
            ret += (n.charAt(i)-'0') * e;
            e *= k;
        }
        
        return ret;
    }
    
    public int toK(int num, int k) {
        int tmp = 0;
        int e = 1;
        while (num > 0) {
            tmp += (num % k) * e;
            num /= k;
            e *= 10;
        }
        return tmp;
    }
    
    public void check(String expression, boolean[] arr) {
        String[] ops = expression.split(" ");
        
        String a = ops[0];
        String b = ops[2];
        String c = ops[4];
        
        for (int i=2;i<=9;i++) {
            if (!arr[i]) continue;
            if (ops[1].equals("+") && toNum(a, i) + toNum(b, i) != toNum(c, i)) {
                arr[i] = false;
            }
            else if (ops[1].equals("-") && toNum(a, i) - toNum(b, i) != toNum(c, i)) {
                arr[i] = false;
            }
        }
    }
    
    public String find(String expression, boolean[] arr) {
        String[] ops = expression.split(" ");
        
        int tmp = 10000;
        for (int k = 2; k<=9; k++) {
            if (!arr[k]) continue;
            int x = 0;
            if (ops[1].equals("+")) {
                x = toK(toNum(ops[0], k) + toNum(ops[2], k), k);
            } else {
                x = toK(toNum(ops[0], k) - toNum(ops[2], k), k);
            }
            
            if (tmp == 10000) tmp = x;
            else if (tmp != x) {
                tmp = 10000;
                break;
            }
        }
        
        if (tmp == 10000) return ops[0] + " " + ops[1] + " " + ops[2] + " " + ops[3] + " " + "?";
        return ops[0] + " " + ops[1] + " " + ops[2] + " " + ops[3] + " " + tmp;
    }
    
    public String[] solution(String[] expressions) {
        boolean[] arr = new boolean[10];
        
        int k = 0;
        for (String expression : expressions) {
            k = Math.max(k, getMaxDegit(expression));
        }
    
        
        for (int i=k+1;i<=9;i++) arr[i] = true;
        
        int cnt = 0;
        for (String expression : expressions) {
            if (expression.charAt(expression.length()-1) == 'X') {
                cnt++;
                continue;
            };
            check(expression, arr);
        }
        
        String[] ans = new String[cnt];
        cnt = 0;
        
        for (String expression : expressions) {
            if (expression.charAt(expression.length()-1) != 'X') continue;
            ans[cnt] = find(expression, arr);
            cnt += 1;
        }
        
        return ans;
    }
}