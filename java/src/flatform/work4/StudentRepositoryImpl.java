package flatform.work4;

//StudentRepositoryImpl.java

import flatform.work4.annotations.Valid;
import flatform.work4.entities.Student;

import java.util.HashMap;
import java.util.Map;

public class StudentRepositoryImpl implements StudentRepository{

    private final Map<String, Student> students = new HashMap<>();



    public Student save(@Valid Student student) {
        return students.put(student.getId(), student);
    }

}
