package platform.ex;

import java.util.ArrayList;
import java.util.List;

public class School {
    private String name;
    private List<Student> students;
    public School(String name) {
        this.name = name;
        this.students = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void removeAllStudent() {
        students.clear();
    }
}
