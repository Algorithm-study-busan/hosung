package platform.work8;

public class Person implements MyMovable {
    private String way;

    public Person(String way) {
        this.way = way;
    }

    @Override
    public String moveBy() {
        return String.format("나는 %s로 출근한다.", way);
    }
}
