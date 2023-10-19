package platform.work6.controller;

import platform.work6.annotations.MyAutowired;
import platform.work6.annotations.MyRestController;
import platform.work6.entity.Person;
import platform.work6.service.PersonService;

@MyRestController
public class PersonController {

    @MyAutowired
    private PersonService service;

    public PersonController() {

    }

    public void createPerson(String name, int age) {
        service.save(name, age);
    }

    public Person getPerson(Long id) {
        return service.findById(id);
    }

}
