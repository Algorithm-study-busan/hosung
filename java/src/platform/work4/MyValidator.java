package platform.work4;

import platform.work4.annotations.Email;
import platform.work4.annotations.NotNull;
import platform.work4.annotations.Size;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class MyValidator {

    public static Set<String> validate(Object obj) {
        Set<String> ret = new HashSet<>();
        List<Field> declaredFields = getAllFields(obj.getClass());
        for (Field declaredField : declaredFields) {
            if (declaredField.isAnnotationPresent(NotNull.class)) {
                declaredField.setAccessible(true);
                try {
                    Object value = declaredField.get(obj);
                    if (value == null) {
                        ret.add(declaredField.getAnnotation(NotNull.class).message());
                    }
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                }
            }
            if (declaredField.isAnnotationPresent(Size.class)) {
                declaredField.setAccessible(true);
                try {
                    Object value = declaredField.get(obj);
                    if (value != null) {
                        int length = value.toString().length();
                        Size annotation = declaredField.getAnnotation(Size.class);
                        if (length < annotation.min() || length > annotation.max()) {
                            ret.add(annotation.message());
                        }
                    }
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                }
            }
            if (declaredField.isAnnotationPresent(Email.class)) {
                declaredField.setAccessible(true);
                try {
                    Object value = declaredField.get(obj);
                    if (value != null) {
                        String email = value.toString();
                        if (!email.matches("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")) {
                            ret.add(declaredField.getAnnotation(Email.class).message());
                        }
                    }
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                }
            }
        }
        return ret;
    }
    private static List<Field> getAllFields(Class<?> clazz) {
        List<Field> fields = new ArrayList<>();

        while (clazz != null && !clazz.equals(Object.class)) {
            for (Field field : clazz.getDeclaredFields()) {
                fields.add(field);
            }
            clazz = clazz.getSuperclass();
        }

        return fields;
    }


}
