public class note3 {
    public static void main(String[] args) {
        String s = "123+456-789";
        String[] split = s.split("\\+");
        for (String s1 : split) {
            System.out.println(s1);
        }
    }
}
