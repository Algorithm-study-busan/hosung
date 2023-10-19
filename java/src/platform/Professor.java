package platform;

import java.util.Objects;

public class Professor extends Person{
    private String major;
    private String schoolName;

    public Professor(String name, int age, String address,
            String schoolName, String major) {
        super(name, age, address);
        this.major = major;
        this.schoolName = schoolName;
    }

    public String major() {
        return major;
    }

    public String schoolName() {
        return schoolName;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public void setSchoolName(String schoolName) {
        this.schoolName = schoolName;
    }

    @Override
    public String toString() {
        return String.format("%s,%d,%s,%s,%s", getName(), getAge(),
                getAddress(), schoolName(), major()
        );
    }

    @Override
    public boolean equals(Object o) {
        return hashCode() == o.hashCode();
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), major, schoolName);
    }
}
