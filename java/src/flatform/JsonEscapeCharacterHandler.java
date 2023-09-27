package flatform;

public class JsonEscapeCharacterHandler {
    public String handleEscapedCharacters(String str) {
        StringBuilder result = new StringBuilder();
        boolean isEscaping = false;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '\\' && i + 1 < str.length()) {
                char nextChar = str.charAt(i + 1);
                switch (nextChar) {
                    case '"': result.append('"'); i++; break;
                    case '\\': result.append('\\'); i++; break;
                    case '/': result.append('/'); i++; break;
                    case 'b': result.append('\b'); i++; break;
                    case 'f': result.append('\f'); i++; break;
                    case 'n': result.append('\n'); i++; break;
                    case 'r': result.append('\r'); i++; break;
                    case 't': result.append('\t'); i++; break;
                    case 'u':
                        if (i + 5 < str.length()) {
                            String hex = str.substring(i + 2, i + 6);
                            char unicodeChar = (char) Integer.parseInt(hex, 16);
                            result.append(unicodeChar);
                            i += 5;
                        }
                        break;
                    default: result.append(c);
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}
