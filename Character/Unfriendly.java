//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Unfriendly object that extends Character.
* @author Danielle Temples
* @version 1.0
*
*/

public class Unfriendly extends Character {

    /**
    * This method creates an Unfriendly constructer and sets maxHealth to 15.
    * @param name Friendly's name
    */

    public Unfriendly(String name) {
        super(name, 15);
        System.out.println("The name's " + name + ". I'm not friendly.");
    }

    /**
    * This method overrides the interact method from the Character class.
    * @param c character constructer
    */

    @Override
    public void interact(Character c) {
        if (c != this && c != null && health != 0) {
            System.out.println(name + ": What are you looking at " + c.getName() + "!?");
        }
    }

    @Override
    protected void increaseHealth() {
        health += 2;
        if (health > maxHealth) {
            health = maxHealth;
        }
    }

    @Override
    protected void decreaseHealth() {
        health -= 3;
        if (health < 0) {
            health = 0;
        }
    }
}