package platform.work8;

@FunctionalInterface
public interface MyFunction {
    void run();

    static MyFunction getMyFunction(String name) {
        return () -> System.out.println(name + ".run()");
    }

    default void sayHello() {
        System.out.println("Hello");
    }
}
