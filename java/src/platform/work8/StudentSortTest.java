package platform.work8;

public class StudentSortTest {
    public static void main(String[] args) {

        Student s1 = new Student(1, "공부잘하는학생", 4.5F);

        Student s2 = new Student(2, "공부잘못하는학생", 2.5F);



        MyComparable[] list = {s1, s2};

        MySort.sort(list);



        for (Object o : list) System.out.println(o);



        System.out.println("=================================================");





        Person p1 = new Person("bus");

        Person p2 = new Person("subway");



        MyMovable[] list2 = {p1, p2};

        for (MyMovable movable : list2) {

            System.out.println(movable.moveBy());

        }



        System.out.println("=================================================");



    }
}
