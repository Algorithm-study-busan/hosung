package flatform;

import java.util.ArrayList;
import java.util.Scanner;

public class SwitchMain {


    public static void main(String[] args) {
        String[] months = {
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
        };
        Scanner scanner = new Scanner(System.in);
        boolean flag = true;
        ArrayList<String> arr = new ArrayList<>();

        while (flag) {
            String op = scanner.nextLine();
            if (op.length() == 0) continue;
            switch (op.charAt(0)) {
                case 'a' :
                    int idx = Integer.parseInt(op.split(" ")[1]) -1;
                    arr.add(months[idx]);
                    break;
                case 'p':
                    System.out.println(arr);
                    break;
                case 'q':
                    flag = false;
                    System.out.println("Bye");
                    break;
                default:
                    System.out.println("Invalid Command");
            }
        }
    }
}
