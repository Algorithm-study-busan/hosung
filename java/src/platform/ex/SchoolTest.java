package platform.ex;

import java.util.*;
import java.util.stream.Collectors;

public class SchoolTest {
    enum Command {
        ADD, REMOVE, FIND, TOP, CLEAR, LIST, QUIT, INVALID
    }
    private static final Scanner scanner = new Scanner(System.in);
    private static final School school = new School("PNU");
    private static final Map<Command, Runnable> commandMap = new HashMap<>();

    static {
        commandMap.put(Command.ADD, SchoolTest::addStudent);
        commandMap.put(Command.REMOVE, SchoolTest::removeStudent);
        commandMap.put(Command.FIND, SchoolTest::findStudentByYear);
        commandMap.put(Command.TOP, SchoolTest::listTopStudentsByGPA);
        commandMap.put(Command.CLEAR, () -> {
            school.removeAllStudent();
            System.out.println("All students have been removed.");
        });

        commandMap.put(Command.LIST, SchoolTest::listAllStudents);
        commandMap.put(Command.QUIT, () -> System.out.println("Goodbye!"));
        commandMap.put(Command.INVALID, () -> System.out.println("Invalid command!"));
    }
    public static void main(String[] args) {
        while (true) {
            Command cmd = getCommand();
            commandMap.getOrDefault(cmd, commandMap.get(Command.INVALID)).run();
            if (cmd == Command.QUIT) {
                break;
            }
        }
    }
    private static Command getCommand() {
        System.out.print("Enter command: ");
        String input = scanner.next().toUpperCase();
        try {
            return Command.valueOf(input);
        } catch (IllegalArgumentException e) {
            return Command.INVALID;
        }
    }



    // implement your code
    private static void addStudent() {
        String name = scanner.next();
        int year = scanner.nextInt();
        double gpa = scanner.nextDouble();
        school.getStudents().add(new Student(name, year, gpa));
    }

    private static void removeStudent() {
        String studentId = scanner.next();
        System.out.println("Student removed (if present).");
        school.getStudents().removeIf(student -> student.getStudentID().equals(studentId));
    }

    private static void findStudentByYear() {
        int year = scanner.nextInt();
        System.out.printf("Students for year %d:\n", year);
        List<Student> students = school.getStudents().stream().filter(student ->
                student.getYear() == year).collect(Collectors.toList());
        for (Student student : students) {
            System.out.println(student);
        }
    }

    private static void listTopStudentsByGPA() {
        int k = scanner.nextInt();
        System.out.printf("Top %d students by GPA:", k);
        List<Student> sorted = school.getStudents().stream().sorted(
                Comparator.comparing(Student::getGPA).reversed()).collect(Collectors.toList());
        for (int i = 0; i < k; i++) {
            System.out.println(sorted.get(i));
        }
    }

    private static void listAllStudents() {
        List<Student> students = school.getStudents();
        if (students.isEmpty()) {
            System.out.println("No students enrolled.");
            return;
        }
        System.out.println("All students:");
        for (Student student : students) {
            System.out.println(student);
        }
    }
}
