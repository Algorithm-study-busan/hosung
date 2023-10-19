package platform;
import java.lang.reflect.*;
import java.util.HashMap;

public class MyObjectMapper {
    private MyJsonParser parser;
    public MyObjectMapper() {
        this.parser = new MyJsonParser();
    }

    public <T> T readValue(String jsonString, Class<T> clazz) throws Exception {
        Constructor<T> constructor = clazz.getDeclaredConstructor();
        constructor.setAccessible(true);
        T instance = constructor.newInstance();

        HashMap<String, Object> data = parser.parse(jsonString);

        for (Field field : clazz.getDeclaredFields()) {
            if (data.containsKey(field.getName())) {
                field.setAccessible(true);
                field.set(instance, data.get(field.getName()));
            }
        }

        return instance;
    }
}
