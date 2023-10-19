package platform;

import java.util.ArrayList;
import java.util.List;

public abstract class AbstractReportGenerator {
    public final String generate(List<Customer> customers) {
        List<Customer> select = select(customers);
        String report = getReportHeader(select);
        for (Customer customer : select) {
            report += getReportForCustomer(customer);
        }
        report += getReportFooter(select);
        return report;
    }

    protected List<Customer> select (List<Customer> customers) {
        List<Customer> selected = new ArrayList<Customer>();
        for (Customer customer : customers) {
            if (customerReportCondition(customer)) {
                selected.add(customer);
            }
        }
        return selected;
    }
    protected abstract boolean customerReportCondition(Customer customer);
    protected abstract String getReportHeader(List<Customer> customers);
    protected abstract String getReportForCustomer(Customer customer);
    protected abstract String getReportFooter(List<Customer> customers);

}

