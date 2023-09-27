package flatform;

import java.util.Objects;

public class Employee {
    private final String name;
    private final Double salary;

    public Employee(String name, Double salary) {
        this.name = name;
        this.salary = salary;
    }


    public String getName() {
        return this.name;
    }

    public Double getSalary() {
        return this.salary;
    }

    @Override
    public String toString() {
        return String.format("%s %.1f", name, salary);
    }

    @Override
    public boolean equals(Object o) {
        return hashCode() == o.hashCode();
    }


    @Override
    public int hashCode() {
        return Objects.hash(name, salary);
    }
}
