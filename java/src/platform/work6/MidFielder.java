package platform.work6;

public class MidFielder extends Player {
    protected MidFielder(Builder builder) {
        super(builder);
    }

    @Override
    protected int getSpeed() {
        return 100;
    }

    @Override
    public String toString() {
        return super.toString() + "Midfielder";
    }
}
