//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This enum represents a Drink object.
* @author Danielle Temples
* @version 1.0
*
*/

public enum Drink {
    CHOCOLATE("hot chocolate", 1.50), COFFEE("coffee", 2.00), TEA("tea", 1.00), EMPTY("nothing", 0.00);
    private String name;
    private double price;

    private Drink(String n, double p) {
        name = n;
        price = p;
    }

    /**
    *This method gets the name of the drink.
    * @return name
    */

    public String getName() {
        return name;
    }

    /**
    *This method gets the price of the drink.
    * @return price
    */

    public double getPrice() {
        return price;
    }
}