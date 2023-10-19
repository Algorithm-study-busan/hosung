package platform.work6;

public class Defender extends Player {
    @Override
    protected int getSpeed() {
        return 90;
    }

    protected Defender(Builder builder) {
        super(builder);
    }

    public String toString() {
        return super.toString() + "Defender";
    }

}
