class CoffeeTester {
    public static void main(String[] args) {
        /*
        Check initial stats
        The following should print:
        "Today we made 0.00 and used 0"
        */
        CoffeeMachine.stats();

        /*
        The following should print:
        coffee: $2.0
        hot chocolate: $1.5
        tea: $1.0
        nothing: $0.0
        */
        System.out.println("" + Drink.COFFEE.getName() + ": $" + Drink.COFFEE.getPrice());
        System.out.println("" + Drink.CHOCOLATE.getName() + ": $" + Drink.CHOCOLATE.getPrice());
        System.out.println("" + Drink.TEA.getName() + ": $" + Drink.TEA.getPrice());
        System.out.println("" + Drink.EMPTY.getName() + ": $" + Drink.EMPTY.getPrice());


        /*
        The following create two equal cups with equal drinks
        The first drink is set by providing a cup and using the pour method
        The second is set with the setDrink method
        */
        Cup cup = new Cup("Dancing Goats", Drink.EMPTY);
        cup = CoffeeMachine.pour(cup, Drink.COFFEE);
        Cup cup2 = new Cup("Dancing Goats", Drink.EMPTY);
        cup2.setDrink(Drink.COFFEE);

        /*
        This should print:
        "A cup of coffee from Dancing Goats and A cup of coffee from Dancing Goats"
        "Are they equal? true"
        */
        System.out.println("" + cup + " and " + cup2);
        System.out.println("Are they equal? " + cup.equals(cup2));

        /*
        This should print:
        "Today we made 2.00 and used 0"
        This is because we poured one drink of coffee, and both cups
        used were already provided.
        */
        CoffeeMachine.stats();

        //Create 14 cups and pour alternatingly chocolate and tea into each of them
        //You should have to restock cups at some point during this
        for (int i = 0; i < 7; i++) {
            Cup cupp;
            Cup cupp2;
            cupp = CoffeeMachine.pour(Drink.CHOCOLATE);
            cupp2 = CoffeeMachine.pour(Drink.TEA);
            /*
            For the first 6 cups, print their stamp or drink
            This should print:
            Java
            TEA
            Java
            TEA
            Java
            TEA
            */
            if (i < 3) {
                System.out.println(cupp.getStamp());
                System.out.println(cupp2.getDrink());
            }
        }

        /*
        Check that your pour and counting functions work
        This should print:
        "Today we made 19.50 and used 14"
        */
        CoffeeMachine.stats();

        /*
        Now, change the contents of cup 2 so the cups are no longer the same
        This should print:
        "Are the equal? false"
        */
        cup2.setDrink(Drink.EMPTY);
        System.out.println("Are they equal? " + cup.equals(cup2));

        /*
        Now change the contents of cup2 back to coffee, but use .pour on cup
        to change its contents to CHOCOLATE
        They are no longer equal.
        This should print:
        "Are they equal? false"
        "My cup is from Java and it cost 1.5 and it has hot chocolate"
        */
        cup2.setDrink(Drink.COFFEE);
        cup = CoffeeMachine.pour(cup, Drink.CHOCOLATE);
        System.out.println("Are they equal? " + cup.equals(cup2));
        System.out.println("My cup is from " + cup.getStamp() + " and it cost "
            + cup.getDrink().getPrice() + " and it has " + cup.getDrink().getName());

        /*
        Print the stats of the entire test.
        This should print:
        "Today we made 21.00 and used 14"
        */
        CoffeeMachine.stats();
    }
}
/*
What this main method prints overall:

Today we made 0.00 and used 0
coffee: $2.0
hot chocolate: $1.5
tea: $1.0
nothing: $0.0
A cup of coffee from Dancing Goats and A cup of coffee from Dancing Goats
Are they equal? true
Today we made 2.00 and used 0
Java
TEA
Java
TEA
Java
TEA
Today we made 19.50 and used 14
Are they equal? false
Are they equal? false
My cup is from Dancing Goats and it cost 1.5 and it has hot chocolate
Today we made 21.00 and used 14
*/