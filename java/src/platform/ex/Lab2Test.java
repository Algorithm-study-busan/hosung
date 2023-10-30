package platform.ex;

public class Lab2Test {
    public static void main(String[] args) throws IllegalAccessException {

        Book book1 = new Book("Harry Potter", "J.K. Rowling", 1997);
        Book book2 = new Book(book1);
        Book book3 = new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925);

        System.out.println(Book.getNumberOfBooks());

        checkEquality(book1, book2);

        getAttr(book1);

        toJson(book1);

        toJson(book2);



        Article article1 = new Article("Java Foundations", "TechMag", 2023);

        Article article2 = new Article(article1);

        Article article3 = new Article("Well-Designed Work", "Sharon", 2022);

        Article article4 = new Article(article3);



        System.out.println(Article.getNumberOfArticles());

        checkEquality(article1, article2);

        checkEquality(article3, article4);

        getAttr(article1);

        toJson(article1);

        toJson(article3);

    }

    // implement your code

    private static void checkEquality(Object o1, Object o2) {
        System.out.println(o1.equals(o2));
    }

    private static void getAttr(Object o) {
        System.out.println(ReflectionUtility.getAttributes(o));
    }

    private static void toJson(Object o) throws IllegalAccessException {
        System.out.println(JSONUtility.toJSON(o));
    }
}
