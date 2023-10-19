package platform.work4.annotations;

import java.lang.annotation.Retention;
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;
import java.lang.annotation.RetentionPolicy;

@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Size {
    int min() default 0;
    int max() default 2147483647;
    String message() default "Size must be between 0 and 2147483647";

}
