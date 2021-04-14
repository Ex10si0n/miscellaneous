package FilterPattern;

import java.util.ArrayList;
import java.util.List;

public class CriteriaMale implements Criteria {
    @Override
    public List<Person> meetCriteria(List<Person> persons) {
        List<Person> malePerson = new ArrayList<>();
        for (Person person: persons)
            if (person.getGender().equalsIgnoreCase("MALE"))
                malePerson.add(person);
        return malePerson;
    }
}
