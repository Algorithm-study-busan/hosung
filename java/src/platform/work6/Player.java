package platform.work6;

public abstract class Player {
    private String name ;
    private int jerseyNumber ;
    protected int speed ;
    protected Player(Builder builder) {
        name = builder.name;
        jerseyNumber = builder.jerseyNumber;
        speed = builder.speed;
    }

    protected abstract int getSpeed();
    @Override
    public String toString() {
        return String.format("Player Name='%s, JerseyNumber=%d, SPEED=%d, ",
                name, jerseyNumber, getSpeed());
    }

    public static class Builder {
        private String name;
        private int jerseyNumber;
        private int speed;
        private String playerType;

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setJerseyNumber(int jerseyNumber) {
            this.jerseyNumber = jerseyNumber;
            return this;
        }

        public Builder setSpeed(int speed) {
            this.speed = speed;
            return this;
        }

        public Builder setPlayerType(String type) {
            this.playerType = type;
            return this;
        }

        public Player build() {
            switch (playerType.toLowerCase()) {
                case "forward":
                    return new Forward(this);
                case "midfielder":
                    return new MidFielder(this);
                case "defender":
                    return new Defender(this);
                default:
                    throw new IllegalArgumentException("Invalid player type: " + playerType);
            }
        }
    }
}