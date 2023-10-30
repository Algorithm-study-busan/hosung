package platform.ex;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;

public class ReflectionUtility {
    public static List<String> getAttributes(Object obj) {
        List<String> ret = new ArrayList<>();
        Field[] declaredFields = obj.getClass().getDeclaredFields();
        for (Field declaredField : declaredFields) {
            ret.add(declaredField.getName());
        }
        return ret;
    }
}
