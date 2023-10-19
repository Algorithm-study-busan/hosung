package platform.work6;

public class Forward extends Player {
    protected Forward(Builder builder) {
        super(builder);
    }


    @Override
    protected int getSpeed() {
        return 110;
    }

    public String toString() {
        return super.toString() + "Forward";
    }
}
