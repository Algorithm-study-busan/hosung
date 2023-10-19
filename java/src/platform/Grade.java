package platform;

public enum Grade {
    FRESH(1),SOPHOMORE(2),JUNIOR(3),SENIOR(4);

    private int num;

    Grade(int num) {
        this.num = num;
    }

    public int getNum() {
        return num;
    }
}
