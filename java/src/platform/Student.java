package platform;

public class Student extends Person {
    private String schoolName;
    private Grade grade = Grade.FRESH;

    public Student(String name, int age, String address, String schoolName) {
        super(name, age, address);
        this.schoolName = schoolName;
    }

    public String getSchoolName() {
        return schoolName;
    }

    public int getGrade() {
        return grade.getNum();
    }

    public void setSchoolName(String schoolName) {
        this.schoolName = schoolName;
    }

    public void setGrade(Grade grade) {
        this.grade = grade;
    }
}
