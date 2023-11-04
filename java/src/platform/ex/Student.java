package platform.ex;

import java.util.concurrent.atomic.AtomicInteger;

public class Student {
    private static final AtomicInteger COUNTER = new AtomicInteger(0);
    private String studentID;
    private String name ;
    private int year ;
    private double GPA ;
    public Student(String name, int year, double GPA) {
        this.studentID = "PNU2023" + COUNTER.incrementAndGet();
        this.name = name;
        this.year = year;
        this.GPA = GPA;
    }

    public String getStudentID() {
        return studentID;
    }

    public String getName() {
        return name;
    }

    public int getYear() {
        return year;
    }

    public double getGPA() {
        return GPA;
    }

    @Override
    public String toString() {
        return String.format(
                "Student{studentID='%s', name='%s', year=%d grade, GPA=%.1f}",
                studentID, name, year, GPA);
    }
}
