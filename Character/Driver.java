public class Driver {

    public static void main(String[] args) {
        Character f1 = new Friendly("friend1");
        Character f2 = new Friendly("friend2");
        Character u1 = new Unfriendly("unfriend1");
        Character u2 = new Unfriendly("unfriend2");
        Character h1 = new Healer("healer1");
        Character h2 = new Healer("healer2");
        Character a1 = new Attacker("attack1");
        Character a2 = new Attacker("attack2");

        f1.interact(f1);    //shouldn't interact
        f1.interact(f2);
        f1.interact(u1);
        f1.interact(a1);
        f1.interact(h1);

        u1.interact(u1);    //shouldn't interact
        u1.interact(u2);
        u1.interact(f1);
        u1.interact(a1);
        u1.interact(h1);

        h1.interact(h1);    //shouldn't interact
        h1.interact(h2);
        h1.interact(f1);
        h1.interact(a1);
        h1.interact(u1);

        a1.interact(a1);    //shouldn't interact
        a1.interact(a2);
        a1.interact(u1);
        a1.interact(f1);
        a1.interact(h1);

        h1.interact(u1);
        h1.interact(u1);        
        h1.interact(u1);
        h1.interact(u1);
        h1.interact(u1);

        h1.interact(u1);


        //TODO: Create an object of each type
        //TODO: Make sure the constructors output the correct info



        //TODO: Test object interactions. Remember most types have
        // unique interactions with other types.

        // Try having attackers attack healers, other attackers, 
        // themselves, etc. Refer to the homework description to see
        // what each interaction should do! (Or not do.)
    }

}