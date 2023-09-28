package flatform;

import java.util.HashMap;

public class EmployeeRepository {
    private static final  EmployeeRepository INSTANCE = new EmployeeRepository();

    private static final HashMap<String, Employee> employees = new HashMap<>();
    public static EmployeeRepository getInstance() {
        return INSTANCE;
    }

    public void add(Employee employee) {
        employees.put(employee.getName(), employee);
    }
    public boolean contains(Employee employee) {
        return employees.containsKey(employee.getName());
    }

    public Employee get(Employee employee) {
        return employees.get(employee.getName());
    }
}
