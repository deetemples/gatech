//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Cat object that extends Animal.
* @author Danielle Temples
* @version 1.0
*
*/

public class Cat extends Animal {
    private int miceCaught;
    private boolean likesLasagna;

    /**
    * This method creates a Cat constructer that takes in name, price, miceCaught, and likesLasagna.
    * @param name Cat's name
    * @param price Cat's price
    * @param miceCaught how many mice a Cat has caught
    * @param likesLasagna if a Cat likes lasagna
    */

    public Cat(String name, double price, int miceCaught, boolean likesLasagna) {
        super(200, name, price);
        this.miceCaught = miceCaught;
        this.likesLasagna = likesLasagna;
    }

    /**
    * This method creates a Cat constructer that takes in miceCaught and likesLasagna.
    * @param miceCaught how many mice a Cat has caught
    * @param likesLasagna if a Cat likes lasagna
    */

    public Cat(int miceCaught, boolean likesLasagna) {
        this("none", 30.0, miceCaught, likesLasagna);
    }

    /**
    * This method gets Cat's mice caught.
    * @return miceCaught
    */

    public int getMiceCaught() {
        return miceCaught;
    }

    /**
    * This method sets Cat's mice caught.
    * @param miceCaught how many mice a Cat has caught
    */

    public void setMiceCaught(int miceCaught) {
        this.miceCaught = miceCaught;
    }

    /**
    * This method gets Cat's likes lasagna.
    * @return likesLasagna
    */

    public boolean getLikesLasagna() {
        return likesLasagna;
    }

    /**
    * This method sets Cat's likes lasagna.
    * @param likesLasagna if a cat likes lasagna
    */

    public void setLikesLasagna(boolean likesLasagna) {
        this.likesLasagna = likesLasagna;
    }

    /**
    * This method compares one cat's number of mice caught to another's.
    * @param other an Animal object (which is an instance of Cat)
    * @return compare
    */

    public int compareTo(Animal other) {
        int compare;
        compare = super.compareTo(other);
        if (compare == 0 && other instanceof Cat) {
            Cat otherCat = (Cat) other;
            if (otherCat.miceCaught > miceCaught) {
                compare =  1;
            } else if (otherCat.miceCaught < miceCaught) {
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
        return String.format("StoreID: %d, Name: %s, Price: %2.2f, likes Lasagna: %b, Mice Caught: %d.",
            storeId, name, price, likesLasagna, miceCaught);
    }
}