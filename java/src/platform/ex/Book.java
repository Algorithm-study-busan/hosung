package platform.ex;

import java.util.Objects;

public class Book {
    private String title;
    private String author;
    private int yearPublished;
    private static int numberOfBooks = 0;

    public Book(String title, String author, int yearPublished) {
        this.title = title;
        this.author = author;
        this.yearPublished = yearPublished;
        numberOfBooks += 1;
    }

    public Book(Book book) {
        this.title = book.getTitle();
        this.author = book.getAuthor();
        this.yearPublished = book.getYearPublished();
        numberOfBooks += 1;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getYearPublished() {
        return yearPublished;
    }

    public static int getNumberOfBooks() {
        return numberOfBooks;
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (object == null || getClass() != object.getClass()) return false;
        Book book = (Book) object;
        return yearPublished == book.yearPublished && Objects.equals(title, book.title) && Objects.equals(author, book.author);
    }

    @Override
    public int hashCode() {
        return Objects.hash(title, author, yearPublished);
    }
}
