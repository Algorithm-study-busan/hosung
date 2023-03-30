import java.util.ArrayList;
import java.util.List;

public class note2 {


    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(1);
        a.add(5);
        a.add(7);
        a.add(11);

        ArrayList<Integer> b = new ArrayList<>();
        b.add(2);
        b.add(6);

        System.out.println(upperBound(a, 1));

    }

    static List<Integer> f(List<Integer> a) {
        return a;
    }

    public static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b) {
        ArrayList<Integer> ret = new ArrayList<Integer>();

        int ai = 0, bi = 0;
        while (ai < a.size() && bi < b.size()) {
            if (a.get(ai) < b.get(bi)) {
                ret.add(a.get(ai++));
            }
            else {
                ret.add(b.get(bi++));
            }
        }
        while (ai < a.size()) {
            ret.add(a.get(ai++));
        }
        while (bi < b.size()) {
            ret.add(b.get(bi++));
        }
        return ret;
    }
    static int upperBound(List<Integer> arr, int x) {
        int lo = 0;
        int hi = arr.size()-1;

        while (lo <= hi) {
            int mid = (lo + hi)/2;
            System.out.println(lo + " " + mid + " " + hi);
            if (x >= arr.get(mid)) lo = mid+1;
            else hi = mid-1;
        }
        return lo;
    }
}
