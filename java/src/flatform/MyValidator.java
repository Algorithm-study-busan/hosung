package flatform;

import java.lang.reflect.Field;
import java.util.HashSet;
import java.util.Set;

public class MyValidator {
    public static Set<String> validate(Object obj) {

        Set<String> violations = new HashSet<>();

        // Implement validation logic using Reflection
        Field[] declaredFields = obj.getClass().getDeclaredFields();
        for (Field declaredField : declaredFields) {
            if (declaredField.isAnnotationPresent(NotNull.class)) {
                declaredField.setAccessible(true);
                try {
                    Object value = declaredField.get(obj);
                    if (value == null) {
                        violations.add(declaredField.getAnnotation(NotNull.class).message());
                    }
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                }
            }
            if (declaredField.isAnnotationPresent(Size.class)) {
                int min = declaredField.getAnnotation(Size.class).min();
                int max = declaredField.getAnnotation(Size.class).max();
                declaredField.setAccessible(true);
                try {
                    String value = (String) declaredField.get(obj);
                    if (value == null) continue;
                    if (value.length() < min || value.length() > max) {
                        violations.add(declaredField.getAnnotation(Size.class).message());
                    }
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                }
            }
        }
        return violations;
    }
}
