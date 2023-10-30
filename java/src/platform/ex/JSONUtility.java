package platform.ex;

import java.lang.reflect.Field;

public class JSONUtility {
    public static String toJSON(Object obj) throws IllegalAccessException {
        StringBuilder ret = new StringBuilder();
        ret.append("{");
        Field[] declaredFields = obj.getClass().getDeclaredFields();
        for (int i = 0; i < declaredFields.length; i++) {
            declaredFields[i].setAccessible(true);
            String key = declaredFields[i].getName();
            Object value = declaredFields[i].get(obj);
            ret.append(String.format("\"%s\": ", key));
            ret.append(value);
            if (i != declaredFields.length - 1) {
                ret.append(", ");
            }
        }
        ret.append("}");
        return ret.toString();
    }
}
