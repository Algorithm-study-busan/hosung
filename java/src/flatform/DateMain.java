package flatform;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class DateMain {
    public static void main(String[] args) {

        char[] weeks = {'월', '화', '수', '목', '금', '토', '일'};
        Date currentDate = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat(
                "yyyy년 MM월 dd일", Locale.KOREA);
        System.out.println(sdf.format(currentDate));
        sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        System.out.println(sdf.format(currentDate));

        String weekOfMonth = new SimpleDateFormat("F").format(currentDate);
        int dayOfWeek = Integer.parseInt(new SimpleDateFormat("u").format(currentDate))-1;
        System.out.printf("오늘은 이 달의 %s번째 %c요일 입니다.", weekOfMonth, weeks[dayOfWeek]);
    }
}
