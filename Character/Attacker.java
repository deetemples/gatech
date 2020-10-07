//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents an Attacker object that extends Unfriendly.
* @author Danielle Temples
* @version 1.0
*
*/

public class Attacker extends Unfriendly {

    /**
    * This method creates an Attacker constructer.
    * @param name Attacker's name
    */

    public Attacker(String name) {
        super(name);
    }

    /**
    * This method overrides the interact method from the Character class.
    * @param c character constructer
    */

    @Override
    public void interact(Character c) {
        super.interact(c);
        if (c != this && c != null && health != 0) {
            attacker(c);
        }
    }

    private void attacker(Character c) {
        if (c.getHealth() == 0) {
            System.out.println(name + ": You show such weakness " + c.getName() + ".");
        } else {
            c.decreaseHealth();
            if (c.getHealth() > 0) {
                System.out.println(name + ": Now you're only at " + c.getHealth() + " health. How does it feel "
                    + c.getName() + "!?");
            } else {
                System.out.println(name + ": You were no match for me " + c.getName() + ".");
            }
        }
    }
}