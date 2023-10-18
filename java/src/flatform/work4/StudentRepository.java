package flatform.work4;

import flatform.work4.annotations.Valid;
import flatform.work4.entities.Student;

//StudentRepository.java
public interface StudentRepository {

    public Student save(@Valid Student student);

}
