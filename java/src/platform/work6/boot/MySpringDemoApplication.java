package platform.work6.boot;

import platform.work6.annotations.MySpringApplication;
import platform.work6.controller.PersonController;
import platform.work6.core.MyApplicationContext;
import platform.work6.entity.Person;
import platform.work6.service.PersonService;

import java.util.List;

@MySpringApplication
public class MySpringDemoApplication {
    public static void main(String[] args) {

        MyApplicationContext context = MySpringApplicationRunner.run(MySpringDemoApplication.class, args);
        PersonController controller = context.getBean(PersonController.class);

        controller.createPerson("John", 30);
        controller.createPerson("Jane", 25);
        System.out.println(controller.getPerson(1L));

        PersonService service = context.getBean(PersonService.class);
        List<Person> allPersons = service.findAll();
        System.out.println("All Persons: " + allPersons);

        service.delete(1L);
        System.out.println(controller.getPerson(1L));

        context.close();

    }
}
