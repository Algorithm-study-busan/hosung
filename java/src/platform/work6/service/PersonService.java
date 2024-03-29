package platform.work6.service;

import platform.work6.annotations.MyAutowired;
import platform.work6.annotations.MyService;
import platform.work6.entity.Person;
import platform.work6.repository.PersonRepository;

import java.util.List;

@MyService
public class PersonService {
    @MyAutowired
    private PersonRepository repository;

    public PersonService() {

    }

    public Person save(String name, int age) {
        return repository.save(name, age);
    }

    public Person findById(Long id) {
        Person person = repository.findById(id);
        if (person == null) {
            return Person.NullPerson;
        }

        return person;
    }

    public List<Person> findAll() {
        return repository.findAll();
    }

    public void delete(Long id) {

        repository.delete(id);

    }
}
