package platform.work6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NumberRepository {

    private List<Number> data = new ArrayList<>();
    private static NumberRepository instance = new NumberRepository();

    public static NumberRepository getInstance() {
        return instance;
    }

    public <T> void addAll(List<? extends Number> arr) {
        for (Number number : arr) {
            data.add(number);
        }
    }

    public String toString(){
        return data.toString();
    }

    public static void main(String[] args) {
        List<Integer> intData = Arrays.asList(10, -100);
        List<Double> doubleData = Arrays.asList(-5.1, 10.01);
        List<String> strData = Arrays.asList("ab", "cd");
        NumberRepository data = NumberRepository.getInstance();

        data.addAll(intData);
        data.addAll(doubleData);
        //data.addAll(strData); //compile error
        System.out.println(data);
    }
}
