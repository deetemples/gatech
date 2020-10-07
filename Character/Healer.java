//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Healer object that extends Friendly.
* @author Danielle Temples
* @version 1.0
*
*/

public class Healer extends Friendly {

    /**
    * This method creates a Healer constructer.
    * @param name Healer's name
    */

    public Healer(String name) {
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
            healer(c);
        }
    }

    private void healer(Character c) {
        if (c.getHealth() == 0) {
            System.out.println(name + ": I'm sorry " + c.getName() + ". Nothing is working!");
        } else if (c.getHealth() == c.getMaxHealth()) {
            System.out.println(name + ": Hey " + c.getName() + ". You look perfectly fine to me!");
        } else {
            c.increaseHealth();
            System.out.println(name + ": Got you up to " + c.getHealth()
                + " health. Hope you feel better " + c.getName() + "!");
        }
    }
}