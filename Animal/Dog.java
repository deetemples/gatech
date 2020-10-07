//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Dog object that extends Animal.
* @author Danielle Temples
* @version 1.0
*
*/

public class Dog extends Animal {
    private boolean curlyTail;
    private int droolRate;

    /**
    * This method creates a Dog constructer that takes in name, price, curlyTail, and droolRate.
    * @param name Dog's name
    * @param price Dog's price
    * @param curlyTail if the Dog has a curly tail
    * @param droolRate Dog's drool rate
    */

    public Dog(String name, double price, boolean curlyTail, int droolRate) {
        super(100, name, price);
        this.curlyTail = curlyTail;
        this.droolRate = droolRate;
    }

    /**
    * This method creates a Dog constructer that takes in curlyTail and droolRate.
    * @param curlyTail if the Dog has a curly tail
    * @param droolRate Dog's drool rate
    */

    public Dog(boolean curlyTail, int droolRate) {
        this("none", 50.0, curlyTail, droolRate);
    }

    /**
    * This method gets Dog's curly tail.
    * @return curlyTail
    */

    public boolean getCurlyTail() {
        return curlyTail;
    }

    /**
    * This method sets Dog's curlyTail.
    * @param curlyTail if the Dog has a curly tail
    */

    public void setCurlyTail(boolean curlyTail) {
        this.curlyTail = curlyTail;
    }

    /**
    * This method gets Dog's drool rate.
    * @return droolRate
    */

    public int getDroolRate() {
        return droolRate;
    }

    /**
    * This method sets Dog's drool rate.
    * @param droolRate Dog's drool rate
    */

    public void setDroolRate(int droolRate) {
        this.droolRate = droolRate;
    }

    /**
    * This method compares one dog's drool rate to another's.
    * @param other an Animal object (which is an instance of Dog)
    * @return compare
    */

    public int compareTo(Animal other) {
        int compare;
        compare = super.compareTo(other);
        if (compare == 0 && other instanceof Dog) {
            Dog otherDog = (Dog) other;
            if (otherDog.droolRate > droolRate) {
                compare =  1;
            } else if (otherDog.droolRate < droolRate) {
                compare = -1;
            }
        }
        return compare;
    }

    /**
    * This method returns a String of the object.
    * @return String
    */

    public String toString() {
        return String.format("StoreID: %d, Name: %s, Price: %2.2f, Curly Tail: %b, Drool Rate: %d.",
            storeId, name, price, curlyTail, droolRate);
    }
}