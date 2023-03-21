public class LTC_1480 {

    public static int[] runningSum(int[] nums) {
        int sum = 0;
        int[] ret = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            ret[i] = sum;
        }
        return ret;
    }

    public static void main(String[] args) {

    }
}
