package platform.work6;


import java.util.Scanner;

public class AnonymousInnerClassTest {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double value = sc.nextDouble();
        double addValue = sc.nextDouble();
        sc.close();

        SpecificTypeData<Double> doubleType = new SpecificTypeData<Double>(value) {
            @Override
            public void addData(Double data) {
                super.data += data;
            }
        };
        doubleType.addData(addValue);
        System.out.println(doubleType.getData());
    }
}