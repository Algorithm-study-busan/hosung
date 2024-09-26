import java.util.*;

class Solution {
    public Deque<Integer> left_col = new ArrayDeque<>();
    public Deque<Integer> right_col = new ArrayDeque<>();
    public Deque<Deque<Integer>> middle = new ArrayDeque<>();
    public int R;
    public int C;
    
    public void rotate() {
        middle.getFirst().addFirst(left_col.removeFirst());
        right_col.addFirst(middle.getFirst().removeLast());
        middle.getLast().addLast(right_col.removeLast());
        left_col.addLast(middle.getLast().removeFirst());
    }
    
    public void shift() {
        left_col.addFirst(left_col.removeLast());
        right_col.addFirst(right_col.removeLast());
        middle.addFirst(middle.removeLast());
    }
    
    public int[][] solution(int[][] rc, String[] operations) {
        R = rc.length;
        C = rc[0].length;
        
        for (int r=0;r<R;r++) {
            left_col.addLast(rc[r][0]);
            right_col.addLast(rc[r][C-1]);
        }
        
        
        for (int r=0;r<R;r++) {
            Deque<Integer> col = new ArrayDeque<>();
            for (int c=1;c<C-1;c++) {
                col.addLast(rc[r][c]);
            }
            middle.addLast(col);
        }
        
        for (String op : operations) {
            if (op.equals("ShiftRow")) shift();
            else rotate();
        }
        
        int r=0;
        while (!left_col.isEmpty()) {
            rc[r++][0] = left_col.removeFirst(); 
        }
        r = 0;
        while (!right_col.isEmpty()) {
            rc[r++][C-1] = right_col.removeFirst();
        }
        
        for (r=0;r<R;r++) {
            int c = 1;
            while (!middle.getFirst().isEmpty()) {
                rc[r][c++] = middle.getFirst().removeFirst();
            }
            middle.removeFirst();
        }
        
        return rc;
    }
}