//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a CoffeeMachine object.
* @author Danielle Temples
* @version 1.0
*
*/

public class CoffeeMachine {
    private static int cupsUsed = 0;
    private static double sales = 0;
    private static Cup[] cups = new Cup[10];
    private static int cupCounter = 9;


    /**
    * This method gets the stats of the sales & cups used.
    */

    public static void stats() {
        System.out.printf("Today we made %.2f and used %d\n", sales, cupsUsed);
    }

    /**
    * This method sets the drink in the cup and increases sales with price of drink.
    * @return cup
    * @param cup from drink & stamp
    * @param drink type of drink
    */

    public static Cup pour(Cup cup, Drink drink) {
        cup.setDrink(drink);
        sales = drink.getPrice() + sales;
        return cup;
    }

    /**
    * This method stocks the cups if not stocked and shifts number of cups when one has been taken.
    * @return cup
    * @param drink type of drink
    */

    public static Cup pour(Drink drink) {
        if (cups[0] == null) {
            stock();
        }
        Cup cup = pour(cups[cupCounter], drink);
        cups[cupCounter] = null;
        cupCounter--;
        cupsUsed = cupsUsed + 1;
        return cup;
    }

    private static void stock() {
        for (int i = 0; i <= 9; i++) {
            cups[i] = new Cup("Java", Drink.EMPTY);
        }
        cupCounter = 9;
    }
}