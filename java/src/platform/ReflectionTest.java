package platform;

import java.util.Scanner;
import java.lang.reflect.Constructor;

public class ReflectionTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String arg1 = sc.next();
        Double arg2 = sc.nextDouble();
        sc.close();

        String className = "Employee";
        Class[] cArgs = new Class[2];
        cArgs[0] = String.class;
        cArgs[1] = Double.class;

        Employee employee1 = null;
        try {
            Class employeeClass = Class.forName(className);
            Constructor constructor = employeeClass.getConstructor(cArgs);
            employee1 = (Employee) constructor.newInstance(arg1, arg2);
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(employee1);
    }
}