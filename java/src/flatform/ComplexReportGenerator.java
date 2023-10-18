package flatform;

import java.util.List;

public class ComplexReportGenerator extends AbstractReportGenerator{
    @Override
    protected boolean customerReportCondition(Customer customer) {
        return customer.getPoint() >= 100;
    }

    @Override
    protected String getReportHeader(List<Customer> customers) {
        return String.format("고객의 수: %d 명 입니다\n", customers.size());
    }

    @Override
    protected String getReportForCustomer(Customer customer) {
        return String.format("%d: %s\n", customer.getPoint(), customer.getName());
    }

    @Override
    protected String getReportFooter(List<Customer> customers) {
        int sumPoint = 0;
        for (Customer customer : customers) {
            sumPoint += customer.getPoint();
        }
        return String.format("점수 합계: %d\n", sumPoint);
    }
}
