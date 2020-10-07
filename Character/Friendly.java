//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Friendly object that extends Character.
* @author Danielle Temples
* @version 1.0
*
*/

public class Friendly extends Character {

    /**
    * This method creates a Friendly constructer and sets maxHealth to 10.
    * @param name Friendly's name
    */

    public Friendly(String name) {
        super(name, 10);
        System.out.println("Hi my name is " + name + "! I am friendly!");
    }

    /**
    * This method overrides the interact method from the Character class.
    * @param c character constructer
    */

    @Override
    public void interact(Character c) {
        if (c != this && c != null && health != 0) {
            System.out.println(name + ": Hi " + c.getName() + "!");
        }
    }

    @Override
    protected void increaseHealth() {
        health += 4;
        if (health > maxHealth) {
            health = maxHealth;
        }
    }

    @Override
    protected void decreaseHealth() {
        health -= 5;
        if (health < 0) {
            health = 0;
        }
    }
}