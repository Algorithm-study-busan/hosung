package platform.ex;

import java.util.Objects;

public class Article {

    private String title;

    private String publisher;

    private int yearPublished;

    private static int numberOfArticles = 0;

    public Article(String title, String publisher, int yearPublished) {
        this.title = title;
        this.publisher = publisher;
        this.yearPublished = yearPublished;
        numberOfArticles += 1;
    }

    public Article(Article article) {
        this.title = article.getTitle();
        this.publisher = article.getPublisher();
        this.yearPublished = article.getYearPublished();
        numberOfArticles += 1;
    }

    public String getTitle() {
        return title;
    }

    public String getPublisher() {
        return publisher;
    }

    public int getYearPublished() {
        return yearPublished;
    }

    public static int getNumberOfArticles() {
        return numberOfArticles;
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (object == null || getClass() != object.getClass()) return false;
        Article article = (Article) object;
        return yearPublished == article.yearPublished && Objects.equals(title, article.title) && Objects.equals(publisher, article.publisher);
    }

    @Override
    public int hashCode() {
        return Objects.hash(title, publisher, yearPublished);
    }
}
