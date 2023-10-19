package platform.work4;

import platform.work4.annotations.Valid;
import platform.work4.entities.Student;

//StudentRepository.java
public interface StudentRepository {

    public Student save(@Valid Student student);

}
