package platform.work8;

public class Student implements MyComparable{
    private int id;
    private String name;
    private float gpa;

    public Student(int id, String name, float gpa) {
        this.id = id;
        this.name = name;
        this.gpa = gpa;
    }

    @Override
    public int compareTo(Object other) {
        Student otherStudent = (Student) other;
        if (gpa < otherStudent.gpa) return -1;
        else if (gpa == otherStudent.gpa) return 0;
        return 1;
    }

    @Override
    public boolean equal(Object other) {
        return id == ((Student) other).id;
    }

    @Override
    public String toString() {
        return String.format("ID: %5d, Name: %15s, GPA: %5.2f", id, name, gpa);
    }
}
