package platform;

import java.util.*;

public class MyJsonParser {
    private JsonEscapeCharacterHandler escapeHandler;
    public MyJsonParser() {
        this.escapeHandler = new JsonEscapeCharacterHandler();
    }
    public HashMap<String, Object> parse(String jsonString) throws Exception {
        return parseJSONString(escapeHandler.handleEscapedCharacters(jsonString));
    }

    public static String readJSONStringFromKeyBoard() {
        Scanner scanner = new Scanner(System.in);
        StringBuilder ret = new StringBuilder();
        while (true) {
            String line = scanner.nextLine();
            if (line.isEmpty()) {
                break;
            }
            ret.append(line);
        }
        return ret.toString();
    }

    public static HashMap<String, Object> parseJSONString(String jsonString) {
        HashMap<String, Object> ret = new HashMap<>();
        jsonString = jsonString.trim();

        if (jsonString.startsWith("{") && jsonString.endsWith("}")) {
            jsonString = jsonString.substring(1, jsonString.length() - 1).trim();
        }
        List<String> elements = toElements(jsonString);

        for (String element : elements) {
            String[] keyValue = splitKeyValue(element);
            String key = keyValue[0].trim();
            String value = keyValue[1].trim();

            key = key.substring(1, key.length() - 1);
            if (value.startsWith("\"")) {
                value = value.substring(1, value.length() - 1);
                ret.put(key, value);
            } else if (value.startsWith("{")) {
                Object recursiveValue = parseJSONString(value);
                ret.put(key, recursiveValue);
            }
            else if (value.startsWith("[")) {
                List<Object> listValue = new ArrayList<>();
                value = value.substring(1, value.length() - 1).trim();
                List<String> listElements = toElements(value);
                if (listElements.get(0).charAt(0) == '{') {
                    for (String listElement : listElements) {
                        listValue.add(parseJSONString(listElement));
                    }
                }
                else if (listElements.get(0).charAt(0) == '"') {
                    for (String listElement : listElements) {
                        listValue.add(listElement.trim().substring(1, listElement.length() - 1).trim());
                    }
                }
                else {
                    for (String listElement : listElements) {
                        if (listElement.contains(".")) {
                            listValue.add(Double.parseDouble(listElement));
                        } else {
                            listValue.add(Integer.parseInt(listElement));
                        }
                    }
                }
                ret.put(key, listValue);
            }
            else {
                if (value.contains(".")) {
                    double doubleValue = Double.parseDouble(value);
                    ret.put(key, doubleValue);
                } else {
                    int intValue = Integer.parseInt(value);
                    ret.put(key, intValue);
                }
            }
        }
        return ret;
    }

    private static List<String> toElements(String jsonString) {
        int cnt1 = 0;
        int cnt2 = 0;
        List<String> elements = new ArrayList<>();
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < jsonString.length(); i++) {
            char c = jsonString.charAt(i);
            if (c == ',' && cnt1 == 0 && cnt2 == 0) {
                elements.add(builder.toString().trim());
                builder = new StringBuilder();
                continue;
            }
            else if (c == '{') cnt1 += 1;
            else if (c == '}') cnt1 -= 1;
            else if (c == '[') cnt2 += 1;
            else if (c == ']') cnt2 -= 1;
            builder.append(c);
        }
        elements.add(builder.toString().trim());
        return elements;
    }

    private static String[] splitKeyValue(String keyValue) {
        String[] ret = new String[2];
        StringBuilder builder = new StringBuilder();
        int cnt = 0;
        for (int i = 0; i < keyValue.length(); i++) {
            if (keyValue.charAt(i) == '"') cnt += 1;
            else if (keyValue.charAt(i) == ':' && cnt % 2 == 0) {
                ret[0] = builder.toString();
                ret[1] = keyValue.substring(i + 1);
                return ret;
            }
            builder.append(keyValue.charAt(i));
        }
        return ret;
    }

    private static String convertHashMapToJsonString(Object object, int indentLevel) {
        StringBuilder result = new StringBuilder();

        if (object instanceof Map) {
            Map<?, ?> map = (Map<?, ?>) object;
            result.append("{\n");
            int count = 0;
            for (Map.Entry<?, ?> entry : map.entrySet()) {
                result.append(getIndentSpaces(indentLevel + 1))
                        .append("\"").append(entry.getKey()).append("\"")
                        .append(": ")
                        .append(convertHashMapToJsonString(entry.getValue(), indentLevel + 1));

                if (++count < map.size()) {
                    result.append(",");
                }
                result.append("\n");
            }
            result.append(getIndentSpaces(indentLevel)).append("}");
        } else if (object instanceof List) {
            List<?> list = (List<?>) object;

            // 모든 항목이 숫자인지 확인
            boolean allNumbers = list.stream().allMatch(item -> item instanceof Number);

            if (allNumbers) {
                result.append("[");
                for (int i = 0; i < list.size(); i++) {
                    result.append(list.get(i).toString());
                    if (i < list.size() - 1) {
                        result.append(", ");
                    }
                }
                result.append("]");
            } else {
                result.append("[\n");
                for (int i = 0; i < list.size(); i++) {
                    result.append(getIndentSpaces(indentLevel + 1))
                            .append(convertHashMapToJsonString(list.get(i), indentLevel + 1));
                    if (i < list.size() - 1) {
                        result.append(",");
                    }
                    result.append("\n");
                }
                result.append(getIndentSpaces(indentLevel)).append("]");
            }
        } else {
            if (object instanceof String) {
                result.append("\"").append(object).append("\"");
            } else {
                result.append(object.toString());
            }
        }
        return result.toString();
    }

    private static String getIndentSpaces(int indentLevel) {
        StringBuilder spaces = new StringBuilder();
        for (int i = 0; i < indentLevel; i++) {
            spaces.append("  "); // 2 spaces per indent level
        }
        return spaces.toString();
    }
}




