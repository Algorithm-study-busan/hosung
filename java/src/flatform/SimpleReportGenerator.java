package flatform;

import java.util.ArrayList;
import java.util.List;

public class SimpleReportGenerator extends AbstractReportGenerator{
    @Override
    protected boolean customerReportCondition(Customer customer) {
        return true;
    }

    @Override
    protected String getReportHeader(List<Customer> customers) {
        return String.format("고객의 수: %d 명\n", customers.size());
    }

    @Override
    protected String getReportForCustomer(Customer customer) {
        return String.format("%s: %d\n", customer.getName(), customer.getPoint());
    }

    @Override
    protected String getReportFooter(List<Customer> customers) {
        return "\n";
    }
}
