//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Character object.
* @author Danielle Temples
* @version 1.0
*
*/

public abstract class Character {

    protected int health;
    protected int maxHealth;
    protected String name;

    /**
    * This method creates a Character constructer.
    * @param name character's name
    * @param maxHealth character's max health
    */

    public Character(String name, int maxHealth) {
        this.maxHealth = maxHealth;
        health = maxHealth;
        this.name = name;
    }

    /**
    * This method gets the Character's health.
    * @return health
    */

    public int getHealth() {
        return health;
    }

    /**
    * This method sets the Character's health.
    * @param health character's health
    */

    public void setHealth(int health) {
        this.health = health;
    }

    /**
    * This method gets the Character's max health.
    * @return max health
    */

    public int getMaxHealth() {
        return maxHealth;
    }

    /**
    * This method gets the Character's name.
    * @return character's name
    */

    public String getName() {
        return name;
    }

    /**
    * This method allows subclasses of Character to interact with the Character's members.
    * @param c character constructer
    */

    public abstract void interact(Character c);

    protected abstract void increaseHealth();

    protected abstract void decreaseHealth();

    // Define any other abstract or concrete methods here to solve the homework problem.
    // Remember, anything you put here will be inherited by all subclasses and can be overridden!
    // Consider how you can use this to your advantage to store useful information or define useful behavior.


}