//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents an Animal object that implement Comparable (which compares Animals).
* @author Danielle Temples
* @version 1.0
*
*/

public class Animal implements Comparable<Animal> {
    protected int storeId;
    protected String name;
    protected double price;

    /**
    * This method creates an Animal constructer that takes in store ID, name, and price.
    * @param storeId Animal's store ID
    * @param name Animal's name
    * @param price Animal's price
    */

    public Animal(int storeId, String name, double price) {
        this.storeId = storeId;
        this.name = name;
        this.price = price;
    }

    /**
    * This method creates an Animal constructer that takes in store ID.
    * @param storeId Animal's store ID
    */

    public Animal(int storeId) {
        this(storeId, "Buzz", 222.00);
    }

    /**
    * This method gets Animal's store ID.
    * @return store ID
    */

    public int getStoreId() {
        return storeId;
    }

    /**
    * This method sets Animal's store ID.
    * @param storeId Animal's store ID
    */

    public void setStoreId(int storeId) {
        this.storeId = storeId;
    }

    /**
    * This method gets Animal's name.
    * @return name
    */

    public String getName() {
        return name;
    }

    /**
    * This method sets Animal's name.
    * @param name Animal's name
    */

    public void setName(String name) {
        this.name = name;
    }

    /**
    * This method gets Animal's price.
    * @return price
    */

    public double getPrice() {
        return price;
    }

    /**
    * This method sets Animal's price.
    * @param price Animal's price
    */

    public void setPrice(double price) {
        this.price = price;
    }

    /**
    * This method compares one animal's store ID to another's.
    * @param other an Animal object
    * @return -1, 0, 1
    */

    public int compareTo(Animal other) {
        if (other.storeId > storeId) {
            return -1;
        } else if (other.storeId == storeId) {
            return name.compareTo(other.name);
        } else {
            return 1;
        }
    }

    /**
    * This method returns a String of the object.
    * @return String
    */

    public String toString() {
        return String.format("StoreID: %d, Name: %s, Price: %2.2f.", storeId, name, price);
    }
}