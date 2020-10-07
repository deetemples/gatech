//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Drink object.
* @author Danielle Temples
* @version 1.0
*
*/

public class Cup {
    private final String stamp;
    private Drink drink;

    /**
    * This method gets the stamp of the cup.
    * @return stamp
    */

    public String getStamp() {
        return stamp;
    }

    /**
    * This method gets the type of drink in the cup.
    * @return drink
    */

    public Drink getDrink() {
        return drink;
    }

    /**
    * This method sets the type of drink from the user.
    * @param drink type of drink
    */

    public void setDrink(Drink drink) {
        this.drink = drink;
    }

    /**
    * This method sets whether or not the drink & stamp of the cup is the same as the other cup
    * @param other other cup
    * @return if the drink & stamp of the cup equals the other cup
    */

    public boolean equals(Cup other) {
        if (other == null) {
            return false;
        }
        return (this.stamp.equals(other.stamp) && this.drink == other.drink);
    }

    /**
    * This method returns where the cup is from and what it is filled with.
    * @return drink in the cup & brand of the cup
    */

    public String toString() {
        return "A cup of " + drink.getName() + " from " + stamp;
    }

    /**
    * This creates a constructer for cup.
    * @param s stamp
    * @param d drink
    */

    public Cup(String s, Drink d) {
        stamp = s;
        drink = d;
    }
}