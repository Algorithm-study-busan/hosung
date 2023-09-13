package flatform;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class DateTimeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean flag = true;

        while (flag) {
            System.out.println("1. Diff\n" +
                    "2. Add/Sub\n" +
                    "3. Week\n" +
                    "4. Exit");
            int op = scanner.nextInt();
            scanner.nextLine();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            switch (op) {
                case 1 :
                    try {
                        System.out.print("Menu: first date (YYYY-MM-DD): second date (YYYY-MM-DD): ");

                        String d1 = scanner.nextLine();
                        String d2 = scanner.nextLine();
                        LocalDate date1 = LocalDate.parse(d1, formatter);
                        LocalDate date2 = LocalDate.parse(d2, formatter);
                        Period period = Period.between(date1, date2);
                        System.out.printf("Diff: %d days\n", period.getDays());
                    } catch (Exception e) {
                        System.out.println("Invalid date format.");
                    }
                    break;
                case 2 :
                    try {
                        System.out.print("Menu: date (YYYY-MM-DD): days to add/subtract:");
                        String d1 = scanner.nextLine();
                        LocalDate date1 = LocalDate.parse(d1, formatter);
                        int n = scanner.nextInt();
                        scanner.nextLine();
                        System.out.printf("New date: %s\n", date1.plusDays(n));
                    } catch (Exception e) {
                        System.out.println("Invalid date format.");
                    }
                    break;
                case 3 :
                    try {
                        System.out.print("Menu: date (YYYY-MM-DD): ");
                        String d1 = scanner.nextLine();
                        LocalDate date1 = LocalDate.parse(d1, formatter);
                        System.out.printf("Day of the week: %s\n", date1.getDayOfWeek());
                    } catch (Exception e) {
                        System.out.println("Invalid date format.");
                    }
                    break;
                case 4 :
                    System.out.println("Menu: Exiting...");
                    flag = false;
                    break;
            }
        }
    }
}
